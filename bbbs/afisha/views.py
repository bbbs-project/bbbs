from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class EventViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.EventSerializer
    permission_classes = [IsAuthenticated]
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
                taken_seats=Count(
                    'participants__participant'
                )).all().order_by('id')
        return (
            models.Event.objects.annotate(
                booked=Count(
                    'participants__participant', filter=Q(
                        participants__participant=user
                    )
                ),
                taken_seats=Count('participants__participant')
            ).filter(city=user.profile.city_id).order_by('id')
        )


class EventParticipantViewSet(mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.CreateModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    queryset = models.EventParticipant.objects.all()
    serializer_class = serializers.EventParticipantSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('event',)
    search_fields = ('event',)
