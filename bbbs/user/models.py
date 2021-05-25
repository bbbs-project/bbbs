from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from bbbs.common.models import City

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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
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


class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    city = models.ManyToManyField(
        to=City,
        blank=True,
        related_name='user',
        verbose_name='Город(a) пользователя'
    )

    def __str__(self):
        return self.user.username
