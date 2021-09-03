from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication

from django.contrib.auth.models import User

from users.api.serializers import UserSerializer, UserListSerializer
from users.decorators import unauthenticated_user

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class UserListView(generics.ListCreateAPIView):
	queryset			= User.objects.all()
	serializer_class 	= UserListSerializer
	permission_classes	= [permissions.IsAuthenticatedOrReadOnly]

class UserViewSet(generics.CreateAPIView):
	authentication_classes = ()
	permission_classes = ()
	serializer_class = UserSerializer

class LoginView(APIView):
	authentication_classes	= [authentication.SessionAuthentication, authentication.TokenAuthentication]
	permission_classes 		= [permissions.IsAuthenticated]

	def post(self,request):
		username 	= request.data.get("username")
		password	= request.data.get("password")

		user 		= authenticate(username=username, password=password)

		if user:
			return Response({"token":user.auth_token.key})
		else:
			return Response({"error":"Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class ListUsers(APIView):

	def get(self, request, format=None):
		usernames = [user.username for user in User.objects.all()]
		return Response(usernames)

@login_required(login_url='login')
class UserView(viewsets.ViewSet):

	def retrieve(self, request, pk):

		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)

		serialized = UserSerializer(user)
		return Response(serialized.data)

	def list(self):
		queryset        = User.objects.all()
		serialized      = UserSerializer(queryset, many=True)

		return Response(serialized.data)

