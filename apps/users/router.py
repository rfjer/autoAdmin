from rest_framework.routers import DefaultRouter
from .views import UsersViewset, UserRegViewset, UserInfoViewset


user_router = DefaultRouter()
user_router.register(r'userreg', UserRegViewset, base_name="userreg")
user_router.register(r'users', UsersViewset, base_name="users")
user_router.register(r'userinfo', UserInfoViewset, base_name="userinfo")
