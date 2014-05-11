from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    owner_field = 'created_by'

    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # All permissions are only allowed to the owner of the snippet
        if hasattr(obj, self.owner_field):
            return obj.created_by == request.user
        return False