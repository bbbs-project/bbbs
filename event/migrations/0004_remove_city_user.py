# Generated by Django 3.2.2 on 2021-05-21 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_alter_city_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='user',
        ),
    ]
