from rest_framework.routers import DefaultRouter
from .views import GroupsViewset, UserGroupsViewset, GroupMembersViewset


group_router = DefaultRouter()
group_router.register(r'groups', GroupsViewset, base_name="groups")
group_router.register(r'usergroups',UserGroupsViewset, base_name="usergroups")
group_router.register(r'groupmembers', GroupMembersViewset, base_name="groupmembers")
