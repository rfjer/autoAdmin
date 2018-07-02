from rest_framework import  viewsets, response, status
from cabinet.models import Cabinet
from .filter import IdcFilter
from .serializers import IdcSerializer
from .models import Idc



class IdcViewset(viewsets.ModelViewSet):
    """
    list:
    返回idc列表

    create:
    创建idc记录

    retrieve:
    返回idc记录

    destroy
    删除idc记录

    update:
    更新idc记录
    """
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    filter_class = IdcFilter
    filter_fields = ("name",)

    def destroy(self, request, *args, **kwargs):
        ret = {"status": 0}
        instance = self.get_object()

        if Cabinet.objects.filter(idc_id__exact=instance.id).count() != 0:
            ret["status"] = 1
            ret["errmsg"] = "该IDC还有机房记录，不能删除"
            return response.Response(ret, status=status.HTTP_200_OK)

        self.perform_destroy(instance)
        return response.Response(ret, status=status.HTTP_200_OK)