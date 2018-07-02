from rest_framework.routers import DefaultRouter
from .views import ServerViewset, NetwokDeviceViewset, IPViewset, ServerAutoReportViewset, ServerCountViewset


servers_router = DefaultRouter()
servers_router.register(r'servers', ServerViewset, base_name="servers")
servers_router.register(r'network_device', NetwokDeviceViewset, base_name="network_device")
servers_router.register(r'ip', IPViewset, base_name="ip")
servers_router.register(r'ServerAutoReport', ServerAutoReportViewset, base_name="ServerAutoReport")
servers_router.register(r'ServerCount', ServerCountViewset, base_name="ServerCount")