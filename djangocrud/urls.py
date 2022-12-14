
from django.contrib import admin
from django.urls import path

from django.urls import include
from rest_framework import routers
from djangocrud.api import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
