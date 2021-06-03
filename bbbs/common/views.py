from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import City, Profile
from .serializers import CitySerializer, ProfileSerializer


class CityViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = City.objects.all().order_by('-is_primary', 'name')
    serializer_class = CitySerializer


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
