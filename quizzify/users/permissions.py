from rest_framework import permissions

from quizzify.users.const import UserScopes
from quizzify.users.models import User

from .utils import get_user_or_none

class AdminPermission(permissions.BasePermission):
    message = 'Only admins have permission'

    def has_permission(self, request, view):
        user = get_user_or_none(request.user.email)
        if user:
            return user.scope == UserScopes.ADMIN
        return False
