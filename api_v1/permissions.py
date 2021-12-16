from rest_framework.permissions import BasePermission


class HasNFT(BasePermission):
    def has_permission(self, request, view):
        pass
