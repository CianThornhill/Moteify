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
        labels = {
            'emote_img': 'Emote Image',
            'title': 'Emote Title',
            'category': 'Emote Category',
        }
        help_texts = {
            'title': "Maximum 25 characters allowed. Only letters -'s and _'s",
            'emote_img': "Image ratio must be 512 x 512 or 1024 x 1024",
        }

    def clean_emote_img(self):
        emote_img = self.cleaned_data.get('emote_img')
        if emote_img:
            # Open the image file using Pillow
            image = Image.open(emote_img)
            width, height = image.size
            if (width, height) not in ((512, 512), (1024, 1024)):
                raise forms.ValidationError(
                    "Image must be either 512x512 or 1024x1024 pixels.")
        return emote_img
