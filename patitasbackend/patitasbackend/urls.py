from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('db/', include('db.api.urls', namespace='myapi')),
    path('user/', include('users.api.urls', namespace='users_data')),
]

urlpatterns += [
	path('api-auth/', include('rest_framework.urls'))
]
