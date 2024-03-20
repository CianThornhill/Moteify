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

from .utils import is_favourite
from .models import Emote, EMOTE_CATEGORY
from .forms import EmoteForm

from django.contrib import messages


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Emotes(ListView):
    """
    View All Emotes
    """
    template_name = 'emotes/emotes.html'
    model = Emote
    context_object_name = 'emotes'
    extra_context = {'emote_categories': EMOTE_CATEGORY}
    paginate_by = 8


    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    

class EmoteDetail(DetailView):
    """
    View Individual Emote
    is_favourite function defined in utils.py
    """
    template_name = 'emotes/emote_detail.html'
    model = Emote
    context_object_name = 'emote'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        emote = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            context['is_favourite'] = is_favourite(user.id, emote.id)
        else:
            context['is_favourite'] = False

        return context


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
        messages.success(self.request, "Emote added successfully!")
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
    
    def form_valid(self, form):
        messages.success(self.request, "Emote edited successfully!")
        return super().form_valid(form)



class DeleteEmote(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Delete an emote
    """
    model = Emote
    template_name = 'emotes/emote_delete.html'
    success_url = '/emotes/'

    def test_func(self):
        return self.request.user == self.get_object().user
    
    def form_valid(self, form):
        messages.success(self.request, "Emote deleted successfully!")
        return super().form_valid(form)


@login_required
def Favourite_add(request, id):
    """
    Add or Remove a favourite
    """
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
    """
    Favourites List View
    """
    user_favourite_emotes = request.user.favourite.all()

    paginator = Paginator(user_favourite_emotes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'emotes/favourite_emotes.html',
        {'page_obj': page_obj})



@login_required
def My_emotes_list(request):
    """
    My Emotes List View
    """
    user_uploaded_emotes = Emote.objects.filter(user=request.user)

    paginator = Paginator(user_uploaded_emotes, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'emotes/my_emotes.html',
        {'page_obj': page_obj})    

