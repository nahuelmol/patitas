from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.api.views import LoginView, RegisterView, ListUsers, UserViewCreate, UserLogout
from users.api.views import UserView
app_name = 'users_data'

router = routers.SimpleRouter()

login_view		= LoginView.as_view()
register_view	= RegisterView.as_view()
list_users 		= ListUsers.as_view()
logout_view 	= UserLogout.as_view()
profile_view 	= UserView.as_view()

urlpatterns = [
	path('profile/',	profile_view, name='profile'),
	path('login/',		login_view, name='login'),
	path('logout/', 	logout_view, name='logout'),
	path('register/',	register_view, name='register'),
	path('list/',		list_users, name='list'),
]

