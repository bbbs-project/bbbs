from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class City(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    is_primary = models.BooleanField(verbose_name='Столица', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Profile(models.Model):
    class Role(models.TextChoices):
        MENTOR = 'Наставник'
        MODERATOR = 'Модератор'
        REGIONAL_MODERATOR = 'Региональный модератор'
        ADMIN = 'Администратор'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.RESTRICT, verbose_name='Город',
                             default=1, related_name='user')
    role = models.TextField(verbose_name='Роль', choices=Role.choices,
                            default='Наставник')

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()