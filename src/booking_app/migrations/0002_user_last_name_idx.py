# Generated by Django 5.0.4 on 2024-05-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['last_name'], name='last_name_idx'),
        ),
    ]
