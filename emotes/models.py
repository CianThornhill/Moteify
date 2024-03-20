from django import forms

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cloudinary.models import CloudinaryField
from django.core.validators import RegexValidator

# Categories
EMOTE_CATEGORY = (
    ("Happy", "Happy"),
    ("Sad", "Sad"),
    ("Excited", "Excited"),
    ("Love", "Love"),
    ("Angry", "Angry"),
    ("Laughing", "Laughing"),
    ("Cry", "Cry"),
    ("Surprised", "Surprised"),
    ("Confused", "Confused"),
    ("Thumbs Up/Down", "Thumbs Up/Down"),
    ("Celebration", "Celebration"),
    ("Dance", "Dance"),
    ("Cool", "Cool"),
    ("Cute", "Cute"),
    ("Funny", "Funny"),
    ("Other", "Other")
)

# Expression pattern that allows only alphanumeric characters and hyphens
slug_pattern = r'^[a-zA-Z0-9-]+$'

# Validator using RegexValidator
slug_validator = RegexValidator(
    regex=slug_pattern,
    message='Only alphanumeric characters and hyphens are allowed.'
)


class Emote(models.Model):
    """
    Model to create and manage emotes.
    Title validates with slug_pattern variable to ensure Emotes are limited to readable, usable names that can be implemented as URLS, and also adds unique=True to ensure all emotes have unique title.
    """

    user = models.ForeignKey(User, related_name='creator', on_delete=models.CASCADE)
    emote_img = CloudinaryField(default='placeholder', folder='emotes/', null=False, blank=False)
    title = models.CharField(max_length=25, null=False, blank=False, validators=[slug_validator], unique=True)
    category = models.CharField(max_length=50, choices=EMOTE_CATEGORY, default="Happy")
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date']
    
    def __str__(self):
        return str(self.title)

    