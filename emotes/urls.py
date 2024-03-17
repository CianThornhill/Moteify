from django.urls import path
from .views import AddEmote, Emotes, EmoteDetail, DeleteEmote, EditEmote

urlpatterns = [
    path('add/', AddEmote.as_view(), name="add_emote"),
    path('', Emotes.as_view(), name='emotes'),
    path("<slug:pk>/", EmoteDetail.as_view(), name="emote_detail"),
    path("edit/<slug:pk>/", EditEmote.as_view(), name="edit_emote"),
    path("delete/<slug:pk>/", DeleteEmote.as_view(), name="delete_emote"),
]