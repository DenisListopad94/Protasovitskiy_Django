# Generated by Django 5.0.4 on 2024-06-08 13:08

import booking_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0004_room_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='photo',
            field=models.ImageField(null=True, upload_to='hotels_photo/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photo/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(null=True, validators=[booking_app.validators.validate_users_age]),
        ),
    ]
