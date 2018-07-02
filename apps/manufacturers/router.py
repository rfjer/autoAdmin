from rest_framework.routers import DefaultRouter
from .views import ManufacturerViewset, ProductModelViewset


manufacturer_router = DefaultRouter()
manufacturer_router.register(r'manufacturer', ManufacturerViewset, base_name="manufacturer")
manufacturer_router.register(r'product_model', ProductModelViewset, base_name="product_model")
