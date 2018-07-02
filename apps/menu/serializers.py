from rest_framework import serializers

from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    """
    前端视图菜单序列化类
    """
    class Meta:
        model = Menu
        fields = ("id", "path", "icon", "title", "show", "parent")

