from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Story


class StoryBaseView(View):
    model = Story
    fields = '__all__'
    success_url = reverse_lazy('crudocd:all')


class StoryListView(StoryBaseView, ListView):
    """ """


class StoryDetailView(StoryBaseView, DetailView):
    """ """


class StoryCreateView(StoryBaseView, CreateView):
    """ """


class StoryUpdateView(StoryBaseView, UpdateView):
    """ """


class StoryDeleteView(StoryBaseView, DeleteView):
    """ """
