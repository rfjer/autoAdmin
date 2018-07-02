from rest_framework.permissions import DjangoModelPermissions

class ModelPermissions(DjangoModelPermissions):

    def get_custom_perms(self, view, method):
        if hasattr(view, "extra_perm_map"):
            if isinstance(view.extra_perm_map, dict):
                return view.extra_perm_map.get(method,[])
        return []

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if not request.user or (
           not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        perms.extend(self.get_custom_perms(view, request.method))
        return request.user.has_perms(perms)