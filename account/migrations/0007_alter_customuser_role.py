# Generated by Django 3.2.2 on 2021-05-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrator'), ('moderator', 'Moderator'), ('regional moderator', 'Regional moderator'), ('mentor', 'Mentor')], default='mentor', max_length=30),
        ),
    ]
