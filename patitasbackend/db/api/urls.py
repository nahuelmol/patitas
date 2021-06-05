from django.urls import path, include
from . import views

app_name = 'myapi'

router = routers.DefaultRouter()

router.register(r'dogs', views.InterprisesView, basename='dogs')
router.register(r'cats', views.MineralsView, basename='cats')
router.register(r'comments', views.ProyectsView, basename='comments')
router.register(r'posts',views.RegionsView, basename='posts')

urlpatterns = router.urls