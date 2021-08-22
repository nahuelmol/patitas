from rest_framework.response import Response
from rest_framework import viewsets

from django.contrib.auth.models import User
from users.api.serializers import UserSerializer

class UserView(viewsets.ViewSet):
    @staticmethod
    def list(self):
        queryset        = User.objects.all()
        serialized      = UserSerializer(queryset, many=True)
        
        return serialized.data 

class UniqueUser(viewsets.ViewSet):

	@staticmethod
	def show(self):
		queryset		= User.objects.all()
		serialized      = UserSerializer(queryset, many=True)

		return serialized.data