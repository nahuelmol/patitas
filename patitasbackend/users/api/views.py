from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework import generics, permissions, authentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from users.api.serializers import UserCreateSerializer, UserListSerializer, RegisterSerializer
from users.decorators import unauthenticated_user
from users.utils import generate_access_token

from emailer.controllers import sendmessage

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.conf import settings

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
		user_token 	= request.COOKIES.get('access_token')
		old_user 	= 0

		if user_token:
			messages.error(request, 'An users is logged in, first logout, end the current session')

		headers 	= request.META
		email_ 		= request.data.get('email')
		username_ 	= request.data.get('username')
		pass_ 		= request.data.get('password')


		if not email_:
			messages.error(request, 'An email is required for verification process')

		new_user = User(
				email=email_,
				username=username_
				)
		new_user.set_password(pass_)

		try:
			User.objects.get(username=username_)
			old_user = 1
		except Exception as e:
			old_user = 0

		print(new_user)

		if not old_user:
			new_user.save()
		else:
			response = redirect(headers.get('HTTP_REFERER', '/') + 'login')
			response.set_cookie(key='message', value='There already exists a user with that username')

			return  response 

		if new_user:
			access_token = generate_access_token(new_user)
			if access_token:
				response = redirect(headers.get('HTTP_REFERER', '/'))
				response.set_cookie(key='access_token', value=access_token)
				response.data = {'access_token': 'created'}

				sendmessage(email_)
		
				return response
			else:
				response = redirect(headers.get('HTTP_REFERER', '/'))
				response.data = {'access_token':'was not created'}
				return response
		else:
			response = redirect(headers.get('HTTP_REFERER', '/'))
			response.data = {'user':'there is no such user'}
			return response

class LoginView(APIView):

	authentication_classes = [
		authentication.TokenAuthentication]

	permission_classes = [
		permissions.AllowAny]

	def post(self,request):
		username 		= request.data.get('username', None)
		password		= request.data.get('password', None)
		headers 		= request.META
		current_token	= request.COOKIES.get('access_token')

		old_user = 1

		if current_token:
			response = redirect(headers.get('HTTP_REFERER', '/') + 'homepage')
			reponse.set_cookie(key='message',value='You are already logged in')
			return response

		try:
			User.objects.get(username=username)
		except Exception as e:
			old_user = 0

		if old_user == 0:
			response = redirect(headers.get('HTTP_REFERER', '/') + 'login')
			response.set_cookie(key='message',value='That user does not exists')
			return response

		if not password:
			raise AuthenticationFailed("An user password is needed")
		if not username:
			raise AuthenticationFailed("An user username is needed")

		user 		= authenticate(username=username, password=password)

		if user:
			response = redirect(headers.get('HTTP_REFERER', '/') + 'homepage')
			response.set_cookie(key='message',value='successfully, logged in')
			user_access_token = generate_access_token(user)

			if user_access_token:
				response.set_cookie(key='access_token', value=user_access_token,httponly=True)
				return response
			else:
				response.set_cookie(key='message',value='token not generated')
				return response
		else:
			response = redirect(headers.get('HTTP_REFERER', '/') + 'login')
			response.set_cookie(key='message', value='there, authentication failed')
			return response

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
		headers 	= request.META

		for k in request.COOKIES:
			cookies.append(k)
		print(cookies)

		if not user_token:
			raise AuthenticationFailed("unauthenticated user")

		payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])
		user_model = get_user_model()
		user = user_model.objects.filter(id=payload['user_id']).first()

		usernames = [user.username for user in User.objects.all()]

		response = Response()
		response.data = {
			'users':usernames
		}
		return response

class UserLogout(APIView):
	authentication_classes 	= [
		authentication.TokenAuthentication]
	permission_classes 		= [
		permissions.AllowAny]

	def get(self, request):

		user_token  = request.COOKIES.get('access_token', None)
		headers 	= request.META

		if user_token:
			response = redirect(headers.get('HTTP_REFERER', '/login'))
			response.delete_cookie('access_token')
			messages.success(request, 'logged out successfully')
			return response 
		response = redirect(headers.get('HTTP_REFERER', '/homepage'))
		messages.success(request, 'you are already logged out')
		return response

class UserView(APIView):
	authentication_classes 	= [
		authentication.TokenAuthentication]
	permission_classes 		= [
		permissions.AllowAny]

	def get(self, request, pk):

		user_token 	= request.COOKIES.get('access_token')
		headers 	= request.META

		if not user_token:
			raise AuthenticationFailed()

		queryset = User.objects.all()

		if queryset:
			user 		= get_object_or_404(queryset, pk=pk)
			serialized 	= UserSerializer(user)

			if user:
				messages.success(request, 'the user was found')
				response 	= redirect(headers.get('HTTP_REFERER','/profile'))
				return reponse

			messages.error(request, 'the user does not exists')
			response = redirect(headers.get('HTTP_REFERER','/homepage'))
			return response

		messages.error(request, 'error retrieving the user')
		response 	= redirect(headers.get('HTTP_REFERER','/homepage'))
		return reponse

class VerifyUserEmail(APIView):
	def get(self, request):
		headers  		= request.META
		access_token 	= request.COOKIES.get('access_token')

		payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=['HS256'])
		user_model = get_user_model()
		user = user_model.objects.filter(id=payload['user_id']).first()

		print(user.is_staff)
		user.is_staff = True
		user.save()
		print(user.is_staff)

		response = redirect(headers.get('HTTP_REFERER','/')+ 'homepage')
		return response

