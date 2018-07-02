
from .models import Idc
from rest_framework import serializers

class IdcSerializer(serializers.ModelSerializer):
    """
    Idc 模型序列化类
    """
    class Meta:
        model = Idc
        fields = '__all__'