import django_filters
from django.contrib.auth.models import Permission
from django.db.models import Q

class PermissionFilter(django_filters.rest_framework.FilterSet):
    """
    权限过滤类
    """
    name = django_filters.CharFilter(method='search_permission')

    def search_permission(self, queryset, name, value):
        return queryset.filter(Q(codename__icontains=value)|
                               Q(content_type__app_label__icontains=value)|
                               Q(content_type__model__icontains=value))


    class Meta:
        model = Permission
        fields = ['name']