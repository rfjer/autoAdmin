
class ZabbixClientError(Exception):
    pass


class ResponseError(ZabbixClientError):
    pass


class InvalidJSONError(ResponseError):
    pass

class JSONRPCError(ZabbixClientError):

    def __init__(self, *args, **kwargs):
        self.code = kwargs.pop('code', None)
        self.message = kwargs.pop('message', None)
        self.data = kwargs.pop('data', None)

        super(JSONRPCError, self).__init__(*args, **kwargs)