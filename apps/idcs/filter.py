import django_filters

from .models import Idc
from django.db.models import Q


class IdcFilter(django_filters.rest_framework.FilterSet):
    """
    IDC机房过滤类
    """
    name = django_filters.CharFilter(method='search_idc')

    def search_idc(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value)|Q(letter__icontains=value))


    class Meta:
        model  = Idc
        fields = ['name']