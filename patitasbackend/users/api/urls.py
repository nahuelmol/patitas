from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.api.views import LoginView, RegisterView, ListUsers, UserViewCreate, UserLogout

app_name = 'users_data'

router = routers.SimpleRouter()

login_view		= LoginView.as_view()
reg_view		= UserViewCreate.as_view()
register_view	= RegisterView.as_view()
list_users 		= ListUsers.as_view()
logout_view 	= UserLogout.as_view()

urlpatterns = [
	path('login/',	login_view, name='login'),
	path('logout/', 	logout_view, name='logout'),
	path('register/',	register_view, name='register'),
	path('reg/', 		reg_view),
	path('list/',		list_users, name='list'),
]

