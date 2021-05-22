from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Event(models.Model):
    booked = models.BooleanField(default=False)
    address = models.CharField(max_length=100, verbose_name='address')
    contact = models.CharField(max_length=100, verbose_name='Contact')
    title = models.CharField(max_length=50, verbose_name='Event title')
    description = models.TextField()
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    seats = models.PositiveSmallIntegerField()
    city = models.ForeignKey('City', blank=False, on_delete=models.DO_NOTHING, related_name='event')#, limit_choices_to={'user': 12})

    def __str__(self):
        return self.title


class EventParticipant(models.Model):
    participant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
         related_name='event'
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='event'
    )



class City(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя города присутствия проекта BBBS')
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name
