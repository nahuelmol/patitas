from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from users.api.serializers import UserCreateSerializer, UserListSerializer, RegisterSerializer
from users.decorators import unauthenticated_user

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class UserListView(generics.ListCreateAPIView):
	queryset			= User.objects.all()
	serializer_class 	= UserListSerializer
	permission_classes	= [permissions.IsAuthenticatedOrReadOnly]

class UserViewCreate(generics.CreateAPIView):
	authentication_classes = [
		authentication.SessionAuthentication,
		authentication.TokenAuthentication
	]

	permission_classes = ()

	serializer_class = UserCreateSerializer

class RegisterView(APIView):
	authentication_classes = [
		authentication.TokenAuthentication]
	permission_classes = []

	def post(self, request):
		#serializer = RegisterSerializer(data=request.data)

		#if serializer.is_valid():
		user = User(
				email=request.data.get('email'),
				username=request.data.get('username')
				)
		user.set_password(request.data.get('password'))
		user.save()

		if user:
			access_token = str(Token.objects.create(user=user))
			data = {'access_token': access_token}

			print(access_token)

			response = Response(data)
			response.set_cookie(key='access_token', value=access_token)
	
			return response
		else:
			response = Response({'resp':'there is any user'})
			return response
		

class LoginView(APIView):

	authentication_classes = [
		authentication.TokenAuthentication,
		#authentication.SessionAuthentication
    	]

	permission_classes = [
		#permissions.IsAuthenticatedOrReadOnly
	]

	def post(self,request):
		username 	= request.data.get("username")
		password	= request.data.get("password")

		user 		= authenticate(username=username, password=password)

		print(user)

		if user:
			print('The user is: '+ user.username)
			access_token = user.auth_token.key
			data = {'access_token':access_token}

			response = Response(data)
			response.set_cookie(key='access_token', value=access_token)
			return response
		else:
			return Response({"error":"Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		return request.data

class ListUsers(APIView):

	def get(self, request, format=None):
		usernames = [user.username for user in User.objects.all()]
		return Response(usernames)

class UserView(viewsets.ViewSet):

	def retrieve(self, request, pk):

		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)

		serialized = UserSerializer(user)
		return Response(serialized.data)

	def list(self, request):
		queryset        = User.objects.all()
		serialized      = UserSerializer(queryset, many=True)

		return Response(serialized.data)

