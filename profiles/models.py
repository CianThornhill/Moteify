from django.db import models

from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField

from cloudinary.models import CloudinaryField

class Profile(models.Model):
    """ 
    Model for User Profiles 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_image = CloudinaryField(
        folder = "user_images",
        default = None,
        transformation=[
            {'width':512, 'height': 512, 'crop': 'fill'}
        ],
        null=True
    )

    default_image = models.ImageField(
        default="/static/img/user_default.png" 
    )

    display_name = models.CharField(max_length=25, blank=True, null=True)
    bio = RichTextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.user.username + ' Profile'