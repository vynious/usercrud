from rest_framework import permissions
from rest_framework.response import Response
from .models import User

class IsThisMine(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser == True: # checks if requesting user is_superuser
            return True
        if request.data['email'] == str(request.user): 
            return True
        else:
            return False
        
class Master(permissions.BasePermission): # only for superusers to query
    def has_permission(self, request, view):
        if request.user.is_superuser == True:
            return True
        return False