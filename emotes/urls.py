from django.urls import path
from .views import AddEmote, Emotes, EmoteDetail, DeleteEmote, EditEmote, Favourite_add, Favourite_list, My_emotes_list

urlpatterns = [
    path('add/', AddEmote.as_view(), name="add_emote"),
    path('', Emotes.as_view(), name='emotes'),
    path("emote_detail/<slug:pk>/", EmoteDetail.as_view(), name="emote_detail"),
    path("edit/<slug:pk>/", EditEmote.as_view(), name="edit_emote"),
    path("delete/<slug:pk>/", DeleteEmote.as_view(), name="delete_emote"),
    path('fav/<int:id>/', Favourite_add, name='favourite_add'),
    path('favourite_emotes/', Favourite_list, name='favourite_list'),
    path('my_emotes/', My_emotes_list, name='my_emotes'),
]