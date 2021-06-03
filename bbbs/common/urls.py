from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from .views import CityViewSet, ProfileViewSet

v1_router = DefaultRouter()
v1_router.register('cities', CityViewSet, basename='city')
v1_router.register('profile', ProfileViewSet, basename='profile')

patterns_auth = [
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]

urlpatterns = [
    path('v1/', include(patterns_auth)),
    path('v1/', include(v1_router.urls)),
]
