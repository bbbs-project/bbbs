from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

from bbbs.common.models import City

User = settings.AUTH_USER_MODEL


class Tag(models.Model):
    name = models.CharField(max_length=200, verbose_name='тег')

    def __str__(self):
        return self.name


class Place(models.Model):
    GENDER = [
        ('BOY', 'Мальчик'),
        ('GIRL', 'Девочка'),
    ]
    TYPE_OF_REST = [
        ('ACTIVE', 'Активный'),
        ('ENTERTAINMENT', 'Развлекательный'),
        ('COGNITIVE', 'Познавательный'),
    ]
    title = models.CharField(max_length=200, verbose_name='название')
    city = models.ForeignKey(
        City,
        blank=True,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name='recommendation',
    )
    description = models.TextField(
        verbose_name='комментарий',
        help_text='Поделитесь впечатлениями о проведенном времени'
    )
    address = models.CharField(max_length=200, verbose_name='адрес')
    gender = models.CharField(
        max_length=20,
        choices=GENDER,
    )
    type_of_rest = models.CharField(
        max_length=20,
        choices=TYPE_OF_REST,
    )
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name='возраст',
    )
    link = models.URLField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='сайт',
        help_text='Введите адрес сайта',
    )
    image = models.URLField(
        blank=True,
        null=True,
        verbose_name='фото',
        help_text='Добавить фото',
    )
    chosen = models.BooleanField(default=False, verbose_name='выбор наставника')
    type_of_establishment = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='тип заведения',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
