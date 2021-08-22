from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('db.api.urls', namespace='myapi')),
    path('storage/', include('users.api.urls', namespace='users_data'))
]
