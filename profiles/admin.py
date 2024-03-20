from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'bio', 'profile_image_url')

    def profile_image_url(self, obj):
        return obj.profile_image.url if obj.profile_image else None