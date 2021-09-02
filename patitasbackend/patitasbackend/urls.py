from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('db/', include('db.api.urls', namespace='myapi')),
    path('storage/', include('users.api.urls', namespace='users_data'))
=======
    path('api/', include('db.api.urls', namespace='myapi')),
    path('storage/', include('users.api.urls', namespace='users_data')),
    path('apiview/', schema_view)
>>>>>>> 435ce227ac62710f1311689eba1ee383cb750dba
]
