from rest_framework.routers import DefaultRouter
from .views import CabinetViewset


cabinet_router = DefaultRouter()
cabinet_router.register(r'cabinet', CabinetViewset, base_name="cabinet")

