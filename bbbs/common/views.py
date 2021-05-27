from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import City, Profile
from .permission import IsAdminOrReadOnly
from .serializers import CitySerializer, ProfileSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all().order_by('-is_primary')
    serializer_class = CitySerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self):
        obj = get_object_or_404(Profile, user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj
