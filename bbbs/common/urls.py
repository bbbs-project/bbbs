from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

from .views import CityList, ProfileView

patterns_auth = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cities/', CityList.as_view(), name='city'),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]

urlpatterns = [
    path('v1/', include(patterns_auth)),
]
