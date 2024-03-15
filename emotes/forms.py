from django import forms
from .models import Emote
from cloudinary.models import CloudinaryField
from PIL import Image

class EmoteForm(forms.ModelForm):
    """
    Form to Create an Emote
    """
    class Meta:
        model = Emote
        fields = ['emote_img', 'title', 'category']

    def clean_emote_img(self):
        emote_img = self.cleaned_data.get('emote_img')
        if emote_img:
            # Open the image file using Pillow
            image = Image.open(emote_img)
            width, height = image.size
            if (width, height) not in ((512, 512), (1024, 1024)):
                raise forms.ValidationError("Image must be either 512x512 or 1024x1024 pixels.")
        return emote_img
    
    labels = {
        'emote_img': 'Emote Image',
        'title': 'Emote Title',
        'category': 'Emote Category',
    }
