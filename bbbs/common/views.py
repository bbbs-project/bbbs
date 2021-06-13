from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import City, Profile, Tag
from .permission import IsAuthorOrReadOnlyPermission
from .serializers import CitySerializer, ProfileSerializer, TagSerializer
from bbbs.user.models import CustomUser


class CityViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = City.objects.all().order_by('-is_primary', 'name')
    serializer_class = CitySerializer


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnlyPermission)

    def get_object(self):
        if self.request.method == 'GET':
            obj = get_object_or_404(Profile, user=self.request.user)
            return obj
        user = get_object_or_404(CustomUser, pk=self.request.data['user'])
        obj = get_object_or_404(Profile, user=user)
        self.check_object_permissions(self.request, obj)
        return obj


class TagList(generics.ListAPIView):
    queryset = Tag.objects.all().order_by('-name')
    serializer_class = TagSerializer
    pagination_class = None
