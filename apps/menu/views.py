from rest_framework import viewsets, mixins, response, status
from rest_framework.generics import get_object_or_404
from django.contrib.auth.models import Group


from .serializers import MenuSerializer
from .models import Menu
from .common import get_menu_tree


class MenuViewset(viewsets.ModelViewSet):
    """
    前端左侧菜单
    
    retrieve:
    返回指定菜单信息
    
    list:
    返回菜单列表
    
    update:
    更新菜单信息
    
    destroy:
    删除菜单记录
    
    create:
    创建菜单资源
    
    partial_update:
    更新部分字段
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class GroupMenuViewset(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    """
    用户组菜单

    retrieve:
    返回用户组的菜单列表

    update:
    给指定用户组增加菜单，参数mid: menu id

    destroy:
    删除指定组下的菜单，参数mid: menu id
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def process_menu(self, group_permission_queryset, data):
        for record in data:
            try:
                group_permission_queryset.get(pk=record.get("id", None))
                record["status"] = True
            except:
                pass
        return data

    def get_group_menus(self):
        groupobj = self.get_object()
        queryset = groupobj.menu_set.all()
        data = get_menu_tree(queryset)
        return response.Response(data)

    def get_modify_menus(self):
        groupobj = self.get_object()
        group_menu_queryset = groupobj.menu_set.all()
        queryset = Menu.objects.all()
        ret = {}
        ret["data"] = get_menu_tree(queryset,group_menu_queryset)
        ret["permissions"] = [obj.id for obj in group_menu_queryset]
        return response.Response(ret)

    def retrieve(self, request, *args, **kwargs):
        modify = request.GET.get("modify", None)
        if modify is not None:
            return self.get_modify_menus()
        else:
            return self.get_group_menus()

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

        self.check_object_permissions(self.request, obj)
        return obj

    def update(self, request, *args, **kwargs):
        ret = {"status": 0}
        groupobj = self.get_object()
        menu_objects = Menu.objects.filter(pk__in=request.data.get("mid"))
        groupobj.menu_set = menu_objects
        return response.Response(ret, status=status.HTTP_200_OK)
