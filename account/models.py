import jwt
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

from event.models import City


class CustomAccountManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_verified = True
        user.is_staff = True
        user.role = user.ADMIN
        user.save()
        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)


class CustomUser(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    REGIONAL_MODERATOR = 'regional moderator'
    MENTOR = 'mentor'
    ROLES = [
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (REGIONAL_MODERATOR, 'Regional moderator'),
        (MENTOR, 'Mentor')
    ]
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=30,
        choices=ROLES,
        default=MENTOR,
    )
    city = models.ManyToManyField(
        to=City,
        blank=True,
        related_name='user',
        verbose_name='Город(a) пользователя'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomAccountManager()

    class Meta:
        ordering = ['email']

    def get_short_name(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    def natural_key(self):
        return (self.email,)

    def __str__(self):
        return self.email

    @property
    def is_admin_role(self):
        return self.role == self.ADMIN

    @property
    def is_moderator_role(self):
        return self.role == self.MODERATOR

    @property
    def is_regional_moderator_role(self):
        return self.role == self.REGIONAL_MODERATOR
