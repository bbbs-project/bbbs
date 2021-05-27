from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class City(models.Model):
    name = models.CharField(max_length=30)
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ManyToManyField(
        to=City,
        blank=True,
        related_name='user',
        verbose_name='Город(a) пользователя'
    )

    def __str__(self):
        return self.user.username
