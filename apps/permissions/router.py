from rest_framework.routers import DefaultRouter
from .views import PermissionsViewset, GroupPermissionsViewset


permission_router = DefaultRouter()
permission_router.register(r'permissions', PermissionsViewset, base_name="permissions")
permission_router.register(r'grouppermissions', GroupPermissionsViewset, base_name="grouppermissions")