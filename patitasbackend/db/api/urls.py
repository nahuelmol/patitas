from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

from django.conf.urls import url
from django.urls import path

from db.api.views import CatsView, DogsView, PostsView, EventsView, CommentsView

from django.views.generic import TemplateView

schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

app_name = 'myapi'

router = routers.SimpleRouter()


router.register(r'dogs', 		DogsView, basename='dogs')
router.register(r'cats', 		CatsView, basename='cats')
router.register(r'comments', 	CommentsView, basename='comments')
router.register(r'posts',		PostsView, basename='posts')
router.register(r'events', 		EventsView, basename='events')

urlpatterns = [
	path('dogses/', DogsView.as_view({'get':'list'}), name="docs"),
]

urlpatterns += router.urls