from rest_framework.permissions import BasePermission
    class IsViewer(BasePermission):
        def has_permission(self, request, view):
            return request.user.filter(user_type="recruiter").exists()