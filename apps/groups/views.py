from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from users.serializers import UserSerializer
from users.common import get_user_obj


from .serializers import Groupserializer
from .filters import GroupFilter


User = get_user_model()


class GroupsViewset(viewsets.ModelViewSet):
    """
    list:
    返回用户组（角色）列表

    destroy:
    删除角色
    """
    queryset = Group.objects.all()
    serializer_class = Groupserializer
    filter_class = GroupFilter
    filter_fields = ("name",)

    def get_queryset(self):
        queryset = super(GroupsViewset, self).get_queryset()
        queryset = queryset.order_by("id")
        return queryset


class UserGroupsViewset(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    """
    retrieve:
    返回指定用户的所有角色

    update:
    修改当前用户的角色
    """
    queryset = User.objects.all()
    serializer_class = Groupserializer

    def retrieve(self, request, *args, **kwargs):
        user_obj = self.get_object()
        queryset = user_obj.groups.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user_obj = self.get_object()
        gids = request.data.get("gid", [])
        user_obj.groups = Group.objects.filter(id__in=gids)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_queryset(self):
        queryset = super(UserGroupsViewset, self).get_queryset()
        return queryset.order_by("id")


class GroupMembersViewset(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          viewsets.GenericViewSet):
    """
    角色成员管理

    retrieve:
    返回指定组的成员列表

    update:
    往指定组里添加成员

    destroy:
    从指定组里删除成员
    """
    queryset = Group.objects.all()
    serializer_class = UserSerializer


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        queryset = instance.user_set.all()
        username=request.GET.get("username", None)
        if username is not None:
            queryset = queryset.filter(Q(name__icontains=username)|Q(username__icontains=username))
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        ret = {"status":0}
        group_obj = self.get_object()
        userobj = get_user_obj(request.data.get(request.data.get("uid", 0)))
        if userobj is None:
            ret["status"] = 1
            ret["errmsg"] = "用户错误"
        else:
            group_obj.user_set.add(userobj)
        return Response(ret, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        ret = {"status": 0}
        group_obj = self.get_object()
        userobj = get_user_obj(request.data.get("uid", 0))
        if userobj is None:
            ret["status"] = 1
            ret["errmsg"] = "用户错误"
        else:
            group_obj.user_set.remove(userobj)
        return Response(ret, status=status.HTTP_200_OK)