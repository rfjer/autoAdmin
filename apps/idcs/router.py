from rest_framework.routers import DefaultRouter
from .views import IdcViewset


idc_router = DefaultRouter()
idc_router.register(r'idcs', IdcViewset, base_name="idcs")
