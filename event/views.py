from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class ListRetrieveUpdateViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    pass


class EventViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.EventSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('starts_at',)
    search_fields = ('title',)

    def get_queryset(self):
        user = self.request.user
        if user.is_admin_role:
            return models.Event.objects.annotate(
                booked=Count(
                    'participants__participant',
                    filter=Q(participants__participant=user)
                ),
                taken_seats=Count('participants__participant')).all()
        user_cities = user.city.values_list('id')
        return (
            models.Event.objects.annotate(booked=Count('participants__participant', filter=Q(participants__participant=user)),
                                          taken_seats=Count('participants__participant')).filter(city__in=user_cities)
        )


class EventParticipantViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    queryset = models.EventParticipant.objects.all()
    serializer_class = serializers.EventParticipantSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('event',)
    search_fields = ('event',)


class CityViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('is_primary',)
    search_fields = ('name',)
