from django.shortcuts import render
from Django.view.generic import CreateView

from .models import Emote

# Create your views here.

class AddEmote(CreateView):
    """
    Add Emote View
    """
    template_name = 'emotes/add_emote.html'
    model = Emote
    form_class = EmoteForm
    success_url = '/emotes/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEmote, self).form_valid(form)