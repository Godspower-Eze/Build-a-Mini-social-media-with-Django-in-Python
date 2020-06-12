# Generated by Django 3.0.5 on 2020-06-11 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200611_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
