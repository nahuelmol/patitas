from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from django.conf.urls import url
from django.urls import path

from db.api.views import CatsView, DogsListView, PostsView, EventsView, CommentsView

from django.views.generic import TemplateView

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

app_name = 'myapi'

router = routers.SimpleRouter()

urlpatterns = [
	path('dogs/', 			DogsListView.as_view(), name="dogs"),
	path('cats/', 			CatsView.as_view({'get':'list'})),
	path('cats/<int:pk>', 	CatsView.as_view({'get':'retrieve'})),
	path('comments/', 		CommentsView.as_view({'get':'list'})),
	path('comments/<int:pk>',CommentsView.as_view({'get':'retrieve'})),
	path('posts/',			PostsView.as_view({'get':'list'})),
	path('posts/<int:pk>', 	PostsView.as_view({'get':'retrieve'}))
]

urlpatterns += router.urls