from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

from .models import Event, EventParticipant

CustomUser = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.BooleanField(default=False)
    taken_seats = serializers.IntegerField()

    class Meta:
        fields = '__all__'
        model = Event


class EventParticipantSerializer(serializers.ModelSerializer):
    participant = serializers.SlugRelatedField(
        slug_field='id',
        write_only=True,
        queryset=CustomUser.objects.all(),
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        fields = '__all__'
        model = EventParticipant
        validators = [
            validators.UniqueTogetherValidator(
                queryset=EventParticipant.objects.all(),
                fields=['event', 'participant'],
                message='Вы уже записаны на это мероприятие'
            )
        ]

    def validate(self, data):
        """
        Checks if there is available seat, whether event city is in your cities
        """
        event = data['event']
        participant = data['participant']
        if event.city != participant.profile.city:
            raise serializers.ValidationError(
                'Город проведения мероприятия отличается от '
                'города, указанного в вашем профиля'
            )
        taken_seats = event.participants.all().count()
        if taken_seats == event.seats:
            raise serializers.ValidationError(
                'К сожалению, свободных мест не осталось'
            )
        return data
