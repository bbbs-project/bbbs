# Generated by Django 3.2.2 on 2021-06-14 19:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='тег')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(help_text='Поделитесь впечатлениями о проведенном времени', verbose_name='комментарий')),
                ('address', models.CharField(max_length=200, verbose_name='адрес')),
                ('gender', models.CharField(choices=[('BOY', 'Мальчик'), ('GIRL', 'Девочка')], max_length=20)),
                ('type_of_rest', models.CharField(choices=[('ACTIVE', 'Активный'), ('ENTERTAINMENT', 'Развлекательный'), ('COGNITIVE', 'Познавательный')], max_length=20)),
                ('age', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='возраст')),
                ('link', models.URLField(blank=True, help_text='Введите адрес сайта', null=True, verbose_name='сайт')),
                ('image', models.URLField(blank=True, help_text='Добавить фото', null=True, verbose_name='фото')),
                ('chosen', models.BooleanField(default=False, verbose_name='выбор наставника')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recommendation', to='common.city')),
                ('type_of_establishment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='where_to_go.tag', verbose_name='тип заведения')),
            ],
        ),
    ]