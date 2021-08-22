from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from db.api import views

app_name = 'myapi'

router = routers.DefaultRouter()

router.register(r'dogs', 		views.DogsView, basename='dogs')
router.register(r'cats', 		views.CatsView, basename='cats')
router.register(r'comments', 	views.CommentsView, basename='comments')
router.register(r'posts',		views.PostsView, basename='posts')
router.register(r'events', 		views.EventsView, basename='events')

urlpatterns = router.urls