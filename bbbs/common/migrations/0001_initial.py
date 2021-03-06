# Generated by Django 3.2.2 on 2021-06-04 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('is_primary', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'ordering': ['-is_primary'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, related_name='user', to='common.city')),
            ],
        ),
    ]
