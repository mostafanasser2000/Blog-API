from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Read permission for are allowed to any request so we'll always
        # allow GET, HEAD, OPTIONS
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author
