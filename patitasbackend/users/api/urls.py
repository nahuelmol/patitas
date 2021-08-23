from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.api.views import UserView, RegisterView

app_name = 'users_data'

router = routers.DefaultRouter()

login_view		= login_view.as_view()
register_view	= RegisterView.as_view()
all_users 		= UserView.as_view({'get':'list'})
unique_user 	= UserView.as_view({'get':'retrieve'})

router.register(r'register',	register_view, basename='register')
router.register(r'login',		login_view, basename='login')
router.register(r'user', 		all_users, basename='user')
router.register(r'all_users', 	unique_user, basename='all_users')

urlpatterns = router.urls