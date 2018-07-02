from django.contrib.auth.models import Permission, Group

from rest_framework import viewsets, mixins, response, status
from rest_framework.generics import get_object_or_404

from .serializers import PermissionSerializer
from .common import get_permission_obj
from .filters import PermissionFilter

class PermissionsViewset(viewsets.ReadOnlyModelViewSet):
    """
    权限列表 视图类

    list:
    返回permission列表

    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filter_class = PermissionFilter
    filter_fields = ("name",)

    def get_queryset(self):
        queryset = super(PermissionsViewset, self).get_queryset()
        queryset = queryset.order_by("content_type__id")
        return queryset


class GroupPermissionsViewset(viewsets.ReadOnlyModelViewSet,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin):
    """
    用户组权限

    retrieve:
    返回用户组的权限列表

    update:
    给指定用户组增加权限，参数pid: permission id

    destroy:
    删除指定组下的权限，参数pid: permission id
    """

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filter_class = PermissionFilter
    filter_fields = ("name",)

    def process_permission(self, group_permission_queryset, data):
        for record in data:
            try:
                group_permission_queryset.get(pk=record.get("id", None))
                record["status"] = True
            except:
                pass
        return data

    def get_group_permissions(self):
        groupobj = self.get_object()
        queryset = groupobj.permissions.all()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)

    def get_modify_permissions(self):
        groupobj = self.get_object()
        group_permission_queryset = groupobj.permissions.all()
        queryset = Permission.objects.all()
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(self.process_permission(group_permission_queryset, serializer.data))

        serializer = self.get_serializer(queryset, many=True)
        return response.Response(self.process_permission(group_permission_queryset, serializer.data))

    def retrieve(self, request, *args, **kwargs):
        modify = request.GET.get("modify", None)
        if modify is not None:
            return self.get_modify_permissions()
        else:
            return self.get_group_permissions()

    def get_object(self):
        queryset = Group.objects.all()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        ret = {"status": 0}
        groupobj = self.get_object()
        permission_obj = get_permission_obj(request.data.get("pid", ""))
        if permission_obj is None:
            ret["status"] = 1
            ret["errmsg"] = "permission 不存在"
        else:
            groupobj.permissions.add(permission_obj)
        return response.Response(ret, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        ret = {"status": 0}
        groupobj = self.get_object()
        permission_obj = get_permission_obj(request.data.get("pid", ""))
        if permission_obj is None:
            ret["status"] = 1
            ret["errmsg"] = "permission 不存在"
        else:
            groupobj.permissions.remove(permission_obj)
        return response.Response(ret, status=status.HTTP_200_OK)