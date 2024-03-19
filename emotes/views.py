from django.views.generic import (
    CreateView, ListView,
    DetailView, DeleteView,
    UpdateView
)

from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Emote, EMOTE_CATEGORY
from .forms import EmoteForm

from django.contrib import messages
from .utils import is_favourite

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class Emotes(ListView):
    """
    View All Emotes
    """
    template_name = 'emotes/emotes.html'
    model = Emote
    context_object_name = 'emotes'
    extra_context = {'emote_categories': EMOTE_CATEGORY} # Pass EMOTE_CATEGORY to templating
    paginate_by = 8


    def get_queryset(self):
        queryset = super().get_queryset()
        # Get selected category from request
        category = self.request.GET.get('category')
        # Filter queryset based on selected category
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    

class EmoteDetail(DetailView):
    """
    View Individual Emote
    """
    template_name = 'emotes/emote_detail.html'
    model = Emote
    context_object_name = 'emote'

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


class EditEmote(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit an emote
    """
    model = Emote
    template_name = 'emotes/emote_edit.html'
    form_class = EmoteForm
    success_url = '/emotes/'

    def test_func(self):
        return self.request.user == self.get_object().user



class DeleteEmote(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete an emote
    """
    model = Emote
    template_name = 'emotes/emote_delete.html'
    success_url = '/emotes/'

    def test_func(self):
        return self.request.user == self.get_object().user


@login_required
def Favourite_add(request, id):
    emote = get_object_or_404(Emote, id=id)
    if emote.favourites.filter(id=request.user.id).exists():
        emote.favourites.remove(request.user)
        messages.success(
            request, 'Emote removed from favorites!')
    else:
        emote.favourites.add(request.user)
        messages.success(
            request, 'Emote added to favorites')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def Favourite_list(request):
    user_favourite_emotes = request.user.favourite.all()

    paginator = Paginator(user_favourite_emotes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'emotes/favourite_emotes.html',
        {'page_obj': page_obj})


# Repurpose above code for "My Emotes" page
@login_required
def My_emotes_list(request):
    user_uploaded_emotes = Emote.objects.filter(user=request.user)

    paginator = Paginator(user_uploaded_emotes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'emotes/my_emotes.html',
        {'page_obj': page_obj})    
