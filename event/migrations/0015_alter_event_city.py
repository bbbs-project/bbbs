# Generated by Django 3.2.2 on 2021-05-22 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_alter_event_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='city',
            field=models.ForeignKey(limit_choices_to={'user': 12}, on_delete=django.db.models.deletion.DO_NOTHING, related_name='event', to='event.city'),
        ),
    ]