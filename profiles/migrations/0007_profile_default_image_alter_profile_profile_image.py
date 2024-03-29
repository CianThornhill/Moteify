# Generated by Django 4.2.11 on 2024-03-15 10:29

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='default_image',
            field=models.ImageField(default='/static/img/user_default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default=None, max_length=255),
        ),
    ]
