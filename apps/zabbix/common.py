from django.conf import settings

from .api_wrapper import ZabbixServerProxy


def _init():
    s = ZabbixServerProxy(settings.ZABBIX_API)
    s.user.login(user=settings.ZABBIX_ADMIN_USER, password=settings.ZABBIX_ADMIN_PASS)
    return s

s = _init()