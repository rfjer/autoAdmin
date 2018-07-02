from .models import Manufacturer, ProductModel
from rest_framework import serializers

class ManufacturerSerializer(serializers.ModelSerializer):
    """
    制造商序列化类
    """
    class Meta:
        model = Manufacturer
        fields = '__all__'


class ProductModelSerializer(serializers.ModelSerializer):
    """
    产品型号序列化类
    """
    def get_vendor_name(self, obj):
        try:
            return {
                "name": obj.vendor_name,
                "id": obj.id
            }
        except:
            return {}

    def to_representation(self, instance):
        vendor_name = self.get_vendor_name(instance.vendor)
        ret = super(ProductModelSerializer, self).to_representation(instance)
        ret["vendor"] = vendor_name
        return ret

    class Meta:
        model = ProductModel
        fields = '__all__'