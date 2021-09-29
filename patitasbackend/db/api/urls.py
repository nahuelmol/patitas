from rest_framework import routers

from django.conf.urls import url
from django.urls import path

from db.api.views import CatsView, DogsListView, PostsView, EventsView, CommentsView

app_name = 'myapi'

router = routers.SimpleRouter()

urlpatterns = [
	path('dogs/', 			DogsListView.as_view({'get':'list'}), name="dogs"),
	path('dogs/<int:pk>',	DogsListView.as_view({'get':'retrive'})),
	path('dog/create',		DogsListView.as_view({'post':'create'})),
	path('cats/', 			CatsView.as_view({'get':'list'}), name="cats"),
	path('cats/<int:pk>', 	CatsView.as_view({'get':'retrieve'})),
	path('cat/create', 		CatsView.as_view({'post':'create'})),

	path('events/',			EventsView.as_view({'get':'list'})),
	path('events/<int:pk>',	EventsView.as_view({'get':'retrieve'})),
	path('event/create',	EventsView.as_view({'post':'create'})),

	path('comments/', 		CommentsView.as_view({'get':'list'}), name="comments"),
	path('comments/<int:pk>',CommentsView.as_view({'get':'retrieve'})),
	path('comment/create',	CommentsView.as_view({'post':'create'})),
	path('posts/',			PostsView.as_view({'get':'list'}), name="posts"),
	path('posts/<int:pk>', 	PostsView.as_view({'get':'retrieve'})),
	path('post/create',		PostsView.as_view({'post':'create'}))
]

urlpatterns += router.urls