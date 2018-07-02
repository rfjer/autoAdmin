from django.contrib.auth.models import Group

def get_group_obj(gid):
    try:
        return Group.objects.get(pk=gid)
    except Group.DoesNotExist:
        return None