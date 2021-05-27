from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User
from bbbs.afisha.models import Event, EventParticipant


class EventSerializer(serializers.ModelSerializer):
    booked = serializers.SerializerMethodField('get_booked')

    def get_booked(self, obj):
        return True

    class Meta:
        model = Event
        fields = serializers.ALL_FIELDS


class EventParticipantSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = EventParticipant
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=EventParticipant.objects.all(),
                fields=['user', 'event']
            )
        ]
