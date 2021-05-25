from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

v1_router = DefaultRouter()
v1_router.register('afisha/events', views.EventViewSet, basename='events')
v1_router.register('cities', views.CityViewSet, basename='cities')
v1_router.register(
    'afisha/event-participants',
    views.EventParticipantViewSet,
    basename='event_participants'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
