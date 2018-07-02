import logging
import json
import requests

logger = logging.getLogger()

from .exceptions import (
    ZabbixClientError, ResponseError,InvalidJSONError, JSONRPCError
)

def dumps(id_, method, params=None, auth=None):
    rpc_request = {
        'jsonrpc': '2.0',
        'id': id_,
        'method': method,
        "params": {}
    }

    if params is not None:
        rpc_request['params'] = params
    if auth is not None:
        rpc_request['auth'] = auth
    json_str = json.dumps(rpc_request, separators=(',', ':'))
    return json_str

def loads(response):
    try:
        rpc_response = response.json()
    except ValueError as e:
        raise InvalidJSONError(e)

    if not isinstance(rpc_response, dict):
        raise ResponseError('Response is not a dict')

    if 'jsonrpc' not in rpc_response or rpc_response['jsonrpc'] != '2.0':
        raise ResponseError('JSON-RPC version not supported')

    if 'error' in rpc_response:
        error = rpc_response['error']
        if 'code' not in error or 'message' not in error:
            raise ResponseError('Invalid JSON-RPC error object')

        code = error['code']
        message = error['message']
        data = error.get('data', None)

        if data is None:
            exception_message = 'Code: {0}, Message: {1}'.format(code, message)
        else:
            exception_message = ('Code: {0}, Message: {1}, ' +
                                 'Data: {2}').format(code, message, data)
        raise JSONRPCError(exception_message, code=code, message=message,
                           data=data)
    if 'result' not in rpc_response:
        raise ResponseError('Response does not contain a result object')
    return rpc_response


class ZabbixServerProxy(object):

    def __init__(self, url):
        self.url = url if not url.endswith('/') else url[:-1]
        self.url += '/api_jsonrpc.php'
        self.headers = {"Content-Type": "application/json-rpc"}
        self._request_id = 0
        self._auth_token = None
        self._method_hooks = {
            'apiinfo.version': self._no_auth_method,
            'user.login': self._login,
            'user.logout': self._logout
        }

    def __getattr__(self, name):
        return ZabbixObject(name, self)

    def call(self, method, params=None):
        method_lower = method.lower()

        if method_lower in self._method_hooks:
            return self._method_hooks[method_lower](method, params=params)

        return self._call(method, params=params, auth=self._auth_token)

    def _call(self, method, params=None, auth=None):
        self._request_id += 1
        request_data = dumps(self._request_id, method, params=params, auth=auth)
        response = requests.post(self.url, data=request_data,
                          headers=self.headers)
        rpc_response = loads(response)
        return rpc_response['result']

    def _no_auth_method(self, method, params=None):
        return self._call(method, params=params)

    def _login(self, method, params=None):
        self._auth_token = None

        # Save the new token if the request is successful
        self._auth_token = self._call(method, params=params)

        return self._auth_token

    def _logout(self, method, params=None):
        try:
            result = self._call(method, params=params, auth=self._auth_token)
        except ZabbixClientError:
            raise
        finally:
            self._auth_token = None

        return result


class ZabbixObject(object):

    def __init__(self, name, server_proxy):
        self.name = name
        self.server_proxy = server_proxy

    def __getattr__(self, name):
        def call_wrapper(*args, **kwargs):
            if args and kwargs:
                raise ValueError('JSON-RPC 2.0 does not allow both ' +
                                 'positional and keyword arguments')

            method = '{0}.{1}'.format(self.name, name)
            params = args or kwargs or None
            return self.server_proxy.call(method, params=params)

        if name.endswith('_'):
            name = name[:-1]

        return call_wrapper
