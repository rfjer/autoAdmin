#/usr/bin/env python
# 导入菜单

import sys
import os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ops.settings")

import django
django.setup()


from menu.models import Menu

menus = [
    {
        "path": "/",
        "label": "Dashboard",
        "icon": "",
        "show": True,
        "children": []
    },
    {
        "path": "/resources",
        "label": "资源管理",
        "icon": "user",
        "show": True,
        "children": [
            {
                "path": "/idc",
                "label": "IDC机房",
                "icon": "user",
                "show": True,
            },
            {
                "path": "/ip",
                "label": "IP管理",
                "icon": "user",
                "show": False,
            },
            {
                "path": "/product",
                "label": "业务线管理",
                "icon": "user",
                "show": True,
            },
            {
                "path": "/manufacturer",
                "label": "制造商",
                "icon": "user",
                "show": False,
            },
            {
                "path": "/server",
                "label": "服务器",
                "icon": "user",
                "show": True,
            },
            {
                "path": "/product_model",
                "label": "机器型号",
                "icon": "user",
                "show": False,
            },
            {
                "path": "/cabinet",
                "label": "机柜管理",
                "icon": "user",
                "show": True,
            },
            {
                "path": "/network_device",
                "label": "网卡管理",
                "icon": "user",
                "show": False,
            }
        ]
    },
    {
        "path": "/monitor",
        "label": "监控管理",
        "icon": "user",
        "show": True,
        "children": [
            {
                "path": "/zabbix",
                "label": "Zabbix",
                "icon": "",
                "show": True
            }
        ]
    },
    {
        "path": "/users",
        "label": "用户管理",
        "icon": "user",
        "show": True,
        "children": [
            {
                "path": "/group/groupPermission",
                "label": "权限列表",
                "icon": "",
                "show": False,
            },
            {
                "path": "/list",
                "label": "用户列表",
                "icon": "",
                "show": True,
            },
            {
                "path": "/group",
                "label": "角色",
                "icon": "",
                "show": True,
            }
        ]
    }
]

def _import_menu(path, label, icon, show, parent, *args, **kwargs):
    menu = Menu()
    menu.path = path
    menu.title = label
    menu.icon = icon
    menu.show = show
    menu.parent = parent
    menu.save()
    return menu



def import_menus():
    for menu in menus:
        children = menu.pop("children", [])
        menu["parent"] = None
        menu_obj = _import_menu(**menu)
        for child in children:
            child["parent"] = menu_obj
            _import_menu(**child)


def run():
    if Menu.objects.count() != 0:
        print("已经有菜单了，不需要再重复导入！")
        sys.exit(0)

    import_menus()


if __name__ == "__main__":
    run()