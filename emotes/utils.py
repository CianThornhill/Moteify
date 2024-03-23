from django.contrib.auth.models import User
from .models import Emote


def is_favourite(user_id, emote_id):
    user = User.objects.get(id=user_id)
    emote = Emote.objects.get(id=emote_id)
    return emote.favourites.filter(id=user.id).exists()
