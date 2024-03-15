from django.urls import path
from .views import AddEmote

urlpatterns = [
    path('', AddEmote.as_view(), name="add_emote"),
]