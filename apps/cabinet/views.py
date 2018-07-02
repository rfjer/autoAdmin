from rest_framework import  viewsets
from .models import Cabinet
from .serializers import CabinetSerializer
from .filter import CabinetFilter

class CabinetViewset(viewsets.ModelViewSet):
    """
    list:
    返回机柜列表

    create:
    创建机柜记录

    retrieve:
    返回机柜记录

    destroy
    删除机柜记录

    update:
    更新机柜记录
    """
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer
    filter_class = CabinetFilter
    filter_fields = ("name", "idc")
