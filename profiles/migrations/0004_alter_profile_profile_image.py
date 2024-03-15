# Generated by Django 4.2.11 on 2024-03-15 00:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default="{% static 'img/user_default.png' %}", max_length=255),
        ),
    ]
