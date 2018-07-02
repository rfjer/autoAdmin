from django.contrib.auth.models import Permission, ContentType

from rest_framework import serializers


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer()
    status       = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Permission
        fields = ("id", "content_type", "name", "codename", "status")