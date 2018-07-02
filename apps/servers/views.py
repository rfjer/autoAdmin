from rest_framework import mixins, viewsets, permissions, response, status

from .models import Server, NetworkDevice, IP
from .serializers import ServerSerializer, NetworkDeviceSerializer, IPSerializer, AutoReportSerializer
from .filter import ServerFilter, NetworkDeviceFilter, IpFilter


class ServerViewset(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    """
    list:
    获取服务器列表

    create:
    创建服务器

    retrieve:
    获取指定服务器记录

    update:
    修改服务器记录
    """
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    #extra_perms_map = {
    #    "GET": ["products.view_product"]
    #}
    filter_class = ServerFilter
    filter_fields = ('hostname', 'idc', 'cabinet', "service", "server_purpose", "server_type")

    def get_queryset(self):
        queryset = super(ServerViewset, self).get_queryset()
        queryset = queryset.order_by("id")
        return queryset


class NetwokDeviceViewset(viewsets.ReadOnlyModelViewSet):
    """
    list:
    获取网卡列表

    retrieve:
    获取指定网卡记录

    """
    queryset = NetworkDevice.objects.all()
    serializer_class = NetworkDeviceSerializer
    filter_class = NetworkDeviceFilter
    filter_fields = ("name",)


class IPViewset(viewsets.ReadOnlyModelViewSet):
    """
    list:
    获取网卡IP列表


    retrieve:
    获取指定网卡IP记录
    """
    queryset = IP.objects.all()
    serializer_class = IPSerializer
    filter_class = IpFilter
    filter_fields = ("ip_addr",)


class ServerAutoReportViewset(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    """
    agent采集的信息入库
    """
    queryset = Server.objects.all()
    serializer_class = AutoReportSerializer
    permission_classes = (permissions.AllowAny,)


class ServerCountViewset(viewsets.ViewSet,mixins.ListModelMixin):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Server.objects.all()

    def list(self, request, *args, **kwargs):
        data = self.get_server_nums()
        return response.Response(data)

    def get_server_nums(self):
        ret = {
            "count": self.queryset.count(),
            "vm_host_num": self.queryset.filter(server_type__exact=0).count(),
            "phy_host_num": self.queryset.filter(server_type__exact=1).count(),
            "master_host_num": self.queryset.filter(server_type__exact=2).count()
        }
        return ret