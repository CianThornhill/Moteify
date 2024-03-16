from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Emote
from .forms import EmoteForm

# Create your views here.

class Emotes(ListView):
    """
    View All Emotes
    """
    template_name = 'emotes/emotes.html'
    model = Emote
    context_object_name = 'emotes'


class AddEmote(LoginRequiredMixin, CreateView):
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

