from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from users.api.serializers import UserCreateSerializer, UserListSerializer, RegisterSerializer
from users.decorators import unauthenticated_user

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.conf import settings

from users.utils import generate_access_token
import jwt

class UserListView(generics.ListCreateAPIView):
	queryset			= User.objects.all()
	serializer_class 	= UserListSerializer
	permission_classes	= [permissions.IsAuthenticatedOrReadOnly]

class UserViewCreate(generics.CreateAPIView):
	authentication_classes = [
		authentication.TokenAuthentication]

	permission_classes = ()

	serializer_class = UserCreateSerializer

class RegisterView(APIView):
	authentication_classes = [
		authentication.TokenAuthentication]
	permission_classes = [
		permissions.AllowAny]

	def post(self, request):
		new_user = User(
				email=request.data.get('email'),
				username=request.data.get('username')
				)
		new_user.set_password(request.data.get('password'))
		new_user.save()

		if new_user:
			access_token = generate_access_token(new_user)
			data = {'access_token': access_token}

			response = Response(data)
			response.set_cookie(key='access_token', value=access_token)
	
			return response
		else:
			response = Response({'resp':'there is any user'})
			return response
		

class LoginView(APIView):

	authentication_classes = [
		authentication.TokenAuthentication]

	permission_classes = [
		permissions.AllowAny]

	def post(self,request):
		username 	= request.data.get('username', None)
		password	= request.data.get('password', None)

		if not password:
			raise AuthenticationFailed("An user password is needed")
		if not username:
			raise AuthenticationFailed("An user username is needed")

		user 		= authenticate(username=username, password=password)

		if user.is_active:
			print('The user is: '+ user.username)
			user_access_token = generate_access_token(user)

			response = Response()
			response.set_cookie(key='access_token', value=user_access_token,httponly=True)
			response.data = {
				'access_token':user_access_token
			}
			return response
		else:
			return Response({"error":"Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		data = {"server-side":"is not posible to make GET to this endpoint"}
		response = Response()
		response.data = data

		return response

class ListUsers(APIView):
	authentication_classes = [
		authentication.TokenAuthentication]
	permission_classes = [
		permissions.AllowAny]

	def get(self, request, format=None):
		cookies = []
		user_token 	= request.COOKIES.get('access_token')

		for k in request.COOKIES:
			cookies.append(k)
		print(cookies)

		if not user_token:
			raise AuthenticationFailed("unauthenticated user")

		payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
		user_model = get_user_model()
		user = user_model.objects.filter(id=payload['user_id']).first()

		usernames = [user.username for user in User.objects.all()]
		return Response(usernames)

class UserLogout(APIView):
	authentication_classes 	= [
		authentication.TokenAuthentication]
	permission_classes 		= [
		permissions.AllowAny]

	def get(self, request):

		user_token  = request.COOKIES.get('access_token', None)
		print(user_token)
		if user_token:
			response = Response()
			response.delete_cookie('access_token')
			response.data = {
				'message':'logged out successfully'
			}
			return response 
		response = Response()
		response.data = {
			'message':'User is already logged out'
			}
		return response

class UserView(APIView):
	authentication_classes 	= [
		authentication.TokenAuthentication]
	permission_classes 		= [
		permissions.AllowAny]

	def get(self, request, pk):

		user_token 	= request.COOKIES.get('access_token')

		if not user_token:
			raise AuthenticationFailed()

		queryset = User.objects.all()
		user = get_object_or_404(queryset, pk=pk)

		serialized = UserSerializer(user)
		return Response(serialized.data)

