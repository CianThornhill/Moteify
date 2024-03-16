from django.urls import path
from .views import AddEmote, Emotes, EmoteDetail

urlpatterns = [
    path('', AddEmote.as_view(), name="add_emote"),
    path('emotes/', Emotes.as_view(), name='emotes'),
    path("<slug:pk>/", EmoteDetail.as_view(), name="emote_detail"),
]