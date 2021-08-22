from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from users.api import views

app_name = 'users_data'

router = routers.DefaultRouter()

router.register(r'user', 		views.UserView, basename='user')
router.register(r'all_users', 		views.UniqueUser, basename='all_users')

urlpatterns = router.urls