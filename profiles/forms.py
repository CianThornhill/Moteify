from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Profile

class UserProfileForm(forms.ModelForm):
    
    bio = forms.CharField(widget=RichTextWidget())

    class Meta:
        model = Profile
        fields = ['profile_image', 'display_name', 'bio']


        widget = {
            "description": forms.Textarea(attrs={"rows": 2}),
        }