from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.api.views import LoginView, UserListView, UserViewSet

app_name = 'users_data'

router = routers.SimpleRouter()

login_view		= LoginView.as_view()
register_view	= UserViewSet.as_view()


urlpatterns = [
	path('login/',		login_view, name='login'),
	path('register/',	register_view, name='register'),
	path('userslist/', 	UserListView.as_view())
]


urlpatterns += router.urls