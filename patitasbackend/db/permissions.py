from rest_framework import permissions

class IsUserLoggedIn(permissions.BasePermission):
	def has_object_permissions(self, request, view, obj):
		print(request.user)
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return obj.owner == request.user