from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('db.api.urls', namespace='myapi')),
    path('storage/', include('users.api.urls', namespace='users_data')),
    path('apiview/', schema_view)
]
