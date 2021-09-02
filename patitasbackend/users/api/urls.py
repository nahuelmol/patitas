from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.api.views import LoginView, UserViewSet

app_name = 'users_data'

router = routers.SimpleRouter()

login_view		= LoginView.as_view()
register_view	= UserViewSet.as_view()
#all_users 		= UserView.as_view({'get':'list'})
#unique_user 	= UserView.as_view({'get':'retrieve'})

#router.register(r'user', 		all_users, basename='user')
#router.register(r'all_users', 	unique_user, basename='all_users')

urlpatterns = [
	path('login/',		login_view, name='login'),
	path('register/',	register_view, name='register')
]

urlpatterns += router.urls