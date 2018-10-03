from rest_framework import permissions


class IsEmployee(permissions.BasePermission):
    message = "You must be and employee to access."
    # safe_methods = ['GET']

    def has_permission(self, request, view):
        # if request.method in self.safe_methods:
        #     return True

        user = request.user
        if user.is_authenticated:
            return user and (request.user.is_employee or request.user.is_staff)

        return False
