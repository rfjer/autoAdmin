import django_filters

from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()

class UserFilter(django_filters.rest_framework.FilterSet):
    """
    用户过滤类
    """
    username = django_filters.CharFilter(method='search_username')

    def search_username(self, queryset, name, value):
        return queryset.filter(Q(name__icontains=value)|Q(username__icontains=value))


    class Meta:
        model = User
        fields = ['username']