from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    REGIONAL_MODERATOR = 'regional moderator'
    MENTOR = 'mentor'


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(
        max_length=30,
        choices=UserRole.choices,
        default=UserRole.MENTOR,
    )

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

    @property
    def is_admin_role(self):
        return self.role == UserRole.ADMIN

    @property
    def is_moderator_role(self):
        return self.role == UserRole.MODERATOR

    @property
    def is_regional_moderator_role(self):
        return self.role == UserRole.REGIONAL_MODERATOR

    @property
    def is_mentore_role(self):
        return self.role == UserRole.MENTOR
