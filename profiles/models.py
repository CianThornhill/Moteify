from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from djrichtextfield.models import RichTextField

from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField

# Create your models here.
class Profile(models.Model):
    """ 
    Model for User Profiles 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField(
        default="/static/img/user_default.png",
        transformation=[
            {'width':512, 'height': 512, 'crop': 'fill'}
        ]
    )
    display_name = models.CharField(max_length=25, blank=True, null=True)
    bio = RichTextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.user.username + ' Profile'