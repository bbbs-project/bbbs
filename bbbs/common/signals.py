from .models import City, Profile
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, **kwargs):
    """ Создаем профиль при создании юзера"""
    instance = kwargs['instance']
    created = kwargs['created']
    if created and not Profile.objects.filter(user=instance).exists() and (
        instance.is_mentore_role
    ):
        try:
            city = City.objects.get(pk=1)
            Profile.objects.create(user=instance, city=city)
        except City.DoesNotExist:
            Profile.objects.create(user=instance)
