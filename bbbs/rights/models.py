from django.db import models
from bbbs.common.models import Tag


class Right(models.Model):
    title = models.CharField(max_length=200, verbose_name='Right title')
    description = models.CharField(max_length=500, verbose_name='Description')
    text = models.TextField()
    color = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
