from django.urls import path
from .views import AddEmote, Emotes

urlpatterns = [
    path('', AddEmote.as_view(), name="add_emote"),
    path('emotes/', Emotes.as_view(), name='emotes'),
]