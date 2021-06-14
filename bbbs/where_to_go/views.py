from django.shortcuts import get_object_or_404

from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from bbbs.common.models import Profile
from .models import Place, Tag
from .serializers import PlaceSerializer, TagSerializer


class TagViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = TagSerializer
    pagination_class = PageNumberPagination
    queryset = Tag.objects.all()


class PlaceListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(chosen=True)


class CreateUpdateViewSet(mixins.CreateModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pass


class PlaceCreateViewSet(CreateUpdateViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        profile = get_object_or_404(Profile, user=self.request.user)
        city = profile.city
        serializer.save(city=city)
