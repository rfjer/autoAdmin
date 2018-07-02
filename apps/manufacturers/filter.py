import django_filters

from .models import Manufacturer, ProductModel


class ManufacturerFilter(django_filters.rest_framework.FilterSet):
    """
    制造商滤类
    """
    vendor_name = django_filters.CharFilter(name="vendor_name", lookup_expr="icontains")

    class Meta:
        model  = Manufacturer
        fields = ['vendor_name']


class ProductModelFilter(django_filters.rest_framework.FilterSet):
    """
    机器型号过滤类
    """
    model_name = django_filters.CharFilter(name="model_name", lookup_expr="icontains")


    class Meta:
        model  = ProductModel
        fields = ['model_name']