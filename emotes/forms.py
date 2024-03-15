from django import forms
from .models import Emote
from cloudinary.models import CloudinaryField

class EmoteForm(forms.ModelForm):
    class Meta:
        model = Emote
        fields = ['emote_img', 'title', 'description', 'category']

    def clean_emote_img(self):
        emote_img = self.cleaned_data.get('emote_img')
        if emote_img:
            width, height = emote_img.width, emote_img.height
            if (width, height) not in ((512, 512), (1024, 1024)):
                raise forms.ValidationError("Image must be either 512x512 or 1024x1024 pixels.")
        return emote_img
