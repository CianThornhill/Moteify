from django.contrib import admin
from .models import Emote

# Register your models here.


@admin.register(Emote)
class EmoteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'get_emote_img_url',
        'title',
        'category',
        'upload_date',
    )

    list_filter = ('user', 'category',)

    def get_emote_img_url(self, obj):
        return obj.emote_img.url if obj.emote_img else None
    get_emote_img_url.short_description = 'Emote Image URL'
