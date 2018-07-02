from django.contrib.auth.models import Permission

def get_permission_obj(pid):
    try:
        return Permission.objects.get(pk=pid)
    except Permission.DoesNotExist:
        return None