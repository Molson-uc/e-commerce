from rest_framework.permissions import BasePermission


class IsClientPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_staff
