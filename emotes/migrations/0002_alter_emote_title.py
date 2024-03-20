# Generated by Django 4.2.11 on 2024-03-20 01:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emote',
            name='title',
            field=models.CharField(max_length=25, unique=True, validators=[django.core.validators.RegexValidator(message='Only alphanumeric characters and hyphens are allowed.', regex='^[a-zA-Z0-9-]+$')]),
        ),
    ]
