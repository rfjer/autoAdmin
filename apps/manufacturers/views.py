from rest_framework import viewsets, response, status
from .models import Manufacturer, ProductModel
from .serializers import ManufacturerSerializer, ProductModelSerializer
from .filter import ManufacturerFilter, ProductModelFilter



class ManufacturerViewset(viewsets.ModelViewSet):
    """
    retrieve:
    返回指定制造商信息
    
    list:
    返回制造商列表
    
    update:
    更新制造商信息
    
    destroy:
    删除制造商记录
    
    create:
    创建制造商资源
    
    partial_update:
    更新部分字段
        
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filter_class = ManufacturerFilter
    filter_fields = ("vendor_name",)

    def destroy(self, request, *args, **kwargs):
        ret = {"status": 0}
        instance = self.get_object()

        if ProductModel.objects.filter(vendor_id__exact=instance.id).count() != 0:
            ret["status"] = 1
            ret["errmsg"] = "该制造商还有产品型号记录，不能删除"
            return response.Response(ret, status=status.HTTP_200_OK)

        self.perform_destroy(instance)
        return response.Response(ret, status=status.HTTP_200_OK)


class ProductModelViewset(viewsets.ModelViewSet):
    """
    retrieve:
    返回指定产品型号信息
    
    list:
    返回产品型号列表
    
    update:
    更新产品型号信息
    
    destroy:
    删除产品型号记录
    
    create:
    创建产品型号资源
    
    partial_update:
    更新部分字段
    """
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    filter_class = ProductModelFilter
    filter_fields = ("model_name",)