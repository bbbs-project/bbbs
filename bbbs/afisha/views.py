from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, serializers

from bbbs.afisha.models import Event, EventParticipant
from bbbs.afisha.serializers import EventSerializer, EventParticipantSerializer
from bbbs.common.models import Profile


class EventList(generics.ListAPIView):
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city__name']

    def get_queryset(self):
        queryset = Event.objects.all().order_by('start_at')
        if self.request.user.is_authenticated:
            profile = get_object_or_404(Profile, user=self.request.user)
            return queryset.filter(city=profile.city)
        return queryset


class EventParticipantList(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer

    def perform_create(self, serializer):
        event = get_object_or_404(Event, id=self.request.data.get('event'))
        if event.participants.count() >= event.seats:
            raise serializers.ValidationError('Все места заняты')
        serializer.save(event=event)
