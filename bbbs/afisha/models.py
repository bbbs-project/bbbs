from django.conf import settings
from django.db import models

from bbbs.common.models import City

User = settings.AUTH_USER_MODEL


class Event(models.Model):
    address = models.CharField(max_length=100, verbose_name='address')
    contact = models.CharField(max_length=100, verbose_name='Contact')
    title = models.CharField(max_length=50, verbose_name='Event title')
    description = models.TextField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    seats = models.PositiveSmallIntegerField()
    city = models.ForeignKey(
        City,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name='event',
    )

    def __str__(self):
        return f'г. {self.city}, {self.title}'


class EventParticipant(models.Model):
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='events'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participants'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['event', 'participant'], name='event'
            )
        ]

    def __str__(self):
        return (f'г. {self.event.city.name} {self.participant.username} '
                f'записан на {self.event.title}')
