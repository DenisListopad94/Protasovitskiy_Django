# Generated by Django 5.0.4 on 2024-05-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_user_last_name_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='hotels',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddIndex(
            model_name='hotels',
            index=models.Index(fields=['stars'], name='stars_idx'),
        ),
        migrations.AddIndex(
            model_name='hotels',
            index=models.Index(fields=['city'], name='city_idx'),
        ),
    ]
