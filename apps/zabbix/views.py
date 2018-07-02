
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework import status, permissions

from servers.models import Server
from .models import Hosts, Functions, Triggers

from products.models import Product


class ZabbixHostStatusViewset(ViewSet, ListModelMixin):
    """
    zabbix status
    """
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        data = {
            "total_host": self.get_total_host_num(),
            "zabbix_total_host": self.get_zabbix_total_host_num(),
            "zabbix_monitor_host": self.get_zabbix_monitor_host_num(),
            "zabbix_not_monitor_host": self.get_zabbix_not_monitor_host_num(),
            "zabbix_monitor_exception_host": self.get_zabbix_monitor_exception_host_num()
        }
        return Response(data, status=status.HTTP_200_OK)


    def get_total_host_num(self):
        """
        返回CMDB中服务器总数
        """
        try:
            return Server.objects.all().count()
        except Exception as e:
            return 0

    def get_zabbix_total_host_num(self):
        """
        返回zabbix中host总数
        """
        try:
            return Hosts.objects.filter(status__in=[0,1]).filter(flags=0).using("zabbix").count()
        except Exception as e:
            return 0

    def get_zabbix_monitor_host_num(self):
        """
        返回zabbix中正常监控的主机数
        """
        try:
            return Hosts.objects.filter(status=0).filter(flags=0).using("zabbix").count()
        except Exception as e:
            return 0

    def get_zabbix_not_monitor_host_num(self):
        """
        return zabbix中，没有监控的主机数
        """
        try:
            return Hosts.objects.filter(status=1).filter(flags=0).using("zabbix").count()
        except Exception as e:
            return 0

    def get_zabbix_monitor_exception_host_num(self):
        """
        return zabbix中，监控异常的主机数： zabbix agent 异常
        """
        try:
            return Hosts.objects.filter(status=0).filter(flags=0).filter(available=2).using("zabbix").count()
        except Exception as e:
            return 0


class ProductHostStatusViewset(ViewSet, ListModelMixin):
    """
    以业务线为维度查看主机状态
    """

    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        data = self.get_product_status()
        return Response(data, status=status.HTTP_200_OK)

    def get_product_status(self):
        ret = []
        for product_obj in Product.objects.filter(pid__exact=0):
            data = {}
            pm = ProductMonitorStatus(product_obj)
            data["name"] = product_obj.service_name
            data["total_host"] = pm.get_host_num()
            data["monitor_total"] = pm.get_monitor_host_num()
            data["not_monitor"] = data["total_host"] - data["monitor_total"]
            data["problem_disaster"] = pm.get_disaster_num()
            data["problem_high"] = pm.get_high_num()
            data["problem_average"] = pm.get_average_num()
            data["problem_warning"] = pm.get_warning_num()
            data["problem_information"] = pm.get_information_num()

            ret.append(data)
        return ret


class ProductMonitorStatus(object):
    def __init__(self, product_obj=None):
        self.product = product_obj
        self.iplist = []        # 业务线下的所有机器的ip地址
        self.hosts = None         # 业务线下的所有机器在zabbix中的 host对象集合
        self.triggerids = None
        self.initialize()


    def initialize(self):
        self.server_queryset = Server.objects.filter(service_id=self.product)
        self.iplist = [obj.manage_ip for obj in self.server_queryset]
        self.hosts = Hosts.objects.filter(interface__ip__in=self.iplist).using("zabbix")

    def get_host_num(self):
        return self.server_queryset.count()

    def get_monitor_host_num(self):
        try:
            return self.hosts.filter(status=0).filter(flags=0).using("zabbix").count()
        except Exception as e:
            return 0


    def get_triggerids(self):
        if self.triggerids is not None:
            return False
        triggerids = []
        try:
            for host in self.hosts:
                for f in Functions.objects.filter(itemid__in=host.items_set.all()).using("zabbix"):
                    triggerids.append(f.triggerid_id)
        except Exception as e:
            pass
        self.triggerids = triggerids

    def get_trigger_queryset(self):
        self.get_triggerids()
        return Triggers.objects.filter(triggerid__in=self.triggerids).filter(value__exact=1).using('zabbix')

    def get_disaster_num(self):
        queryset = self.get_trigger_queryset()
        try:
            return queryset.filter(priority__exact=5).count()
        except Exception as e:
            return 0

    def get_high_num(self):
        queryset = self.get_trigger_queryset()
        try:
            return queryset.filter(priority__exact=4).count()
        except Exception as e:
            return 0

    def get_average_num(self):
        queryset = self.get_trigger_queryset()
        try:
            return queryset.filter(priority__exact=3).count()
        except Exception as e:
            return 0

    def get_warning_num(self):
        queryset = self.get_trigger_queryset()
        try:
            return queryset.filter(priority__exact=2).count()
        except Exception as e:
            return 0

    def get_information_num(self):
        queryset = self.get_trigger_queryset()
        try:
            return queryset.filter(priority__exact=1).count()
        except Exception as e:
            return 0
