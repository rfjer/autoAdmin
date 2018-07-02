from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Product


User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):

    def validate_pid(self, pid):
        if pid > 0:
            try:
                product_obj = Product.objects.get(pk=pid)
                if product_obj.pid != 0:
                    return serializers.ValidationError("上级业务线错误")
            except Product.DoesNotExist:
                return serializers.ValidationError("上级业务线不存在")
            return pid
        else:
            return 0

    def get_user_response(self, user_queryset):
        ret = []
        for dev in user_queryset:
            ret.append({
                "username": dev.username,
                "name": dev.name,
                "email": dev.email,
                "id": dev.id,
            })
        return ret

    def to_representation(self, instance):
        dev_interface = self.get_user_response(instance.dev_interface.all())
        op_interface = self.get_user_response(instance.op_interface.all())
        ret = super(ProductSerializer, self).to_representation(instance)
        ret["dev_interface"] = dev_interface
        ret["op_interface"] = op_interface
        return ret

    def update(self, instance, validated_data):
        instance.service_name = validated_data.get("service_name", instance.service_name)
        instance.module_letter = validated_data.get("module_letter", instance.module_letter)
        instance.dev_interface = validated_data.get("dev_interface", instance.dev_interface)
        instance.op_interface = validated_data.get("op_interface", instance.op_interface)
        instance.save()
        return instance

    class Meta:
        model = Product
        fields = '__all__'
