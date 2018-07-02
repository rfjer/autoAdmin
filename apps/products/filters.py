import django_filters
from .models import Product

class ProductFilter(django_filters.rest_framework.FilterSet):
    """
    业务线过滤类
    """
    pid     = django_filters.NumberFilter(name="pid")


    class Meta:
        model = Product
        fields = ['pid']