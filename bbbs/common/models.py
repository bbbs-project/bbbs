from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class City(models.Model):
    name = models.CharField(max_length=30)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
        ordering = ['-is_primary']


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.RESTRICT,
        related_name='user',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username
