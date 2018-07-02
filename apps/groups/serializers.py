
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

User = get_user_model()

class Groupserializer(serializers.ModelSerializer):
    """
    group序列化类
    """
    def to_representation(self, instance):
        member = instance.user_set.count()
        ret = super(Groupserializer, self).to_representation(instance)
        ret["member"] = member
        return ret


    class Meta:
        model = Group
        fields = ("id", "name")

class UserGroupsSerializer(serializers.ModelSerializer):
    """
    用户的角色 序列化类
    """
    groups = Groupserializer(many=True)

    def to_representation(self, instance):
        name = instance.name
        ret = super(UserGroupsSerializer, self).to_representation(instance)
        ret["name"] = name
        return ret

    class Meta:
        model = User
        fields = ("id", "username", "groups")