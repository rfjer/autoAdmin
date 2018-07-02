import django_filters
from django.contrib.auth.models import Group

class GroupFilter(django_filters.rest_framework.FilterSet):
    """
    用户组过滤类
    """
    name = django_filters.CharFilter(name='name',lookup_expr='icontains')


    class Meta:
        model = Group
        fields = ['name']

