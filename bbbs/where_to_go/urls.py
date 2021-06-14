from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

v1_router = DefaultRouter()
v1_router.register('places', views.PlaceListViewSet, basename='places')
v1_router.register('places/tags', views.TagViewSet, basename='tags')
v1_router.register('place', views.PlaceCreateViewSet, basename='place')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
