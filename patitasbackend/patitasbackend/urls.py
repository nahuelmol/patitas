from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view

urlpatterns = [
	path('api-schemas', get_schema_view(title='API Schema', description='Guide for the REST API'), name='api_schema'),
    path('admin/', admin.site.urls),
    path('db/', include('db.api.urls', namespace='myapi')),
    path('user/', include('users.api.urls', namespace='users_data')),
    path('swagger-ui/', TemplateView.as_view(
    	template_name='docs.html',
    	extra_context={'schema_url':'api_schema'}
    	), name='swagger-ui'),
]

urlpatterns += [
	path('api-auth/', include('rest_framework.urls'))
]
