from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Audio, Domaine
from django.urls import reverse_lazy

# Vues pour l'entité "audio"
class AudioListView(ListView):
    model = Audio
    template_name = 'audio_list.html'
    context_object_name = 'audios'

class AudioDetailView(DetailView):
    model = Audio
    template_name = 'audio_detail.html'
    context_object_name = 'audio'

class AudioCreateView(CreateView):
    model = Audio
    template_name = 'audio_form.html'
    fields = ['domaine', 'audio', 'date', 'auteur']

class AudioUpdateView(UpdateView):
    model = Audio
    template_name = 'audio_form.html'
    fields = ['domaine', 'audio', 'date', 'auteur']

class AudioDeleteView(DeleteView):
    model = Audio
    template_name = 'audio_confirm_delete.html'
    success_url = reverse_lazy('audio_list')

# Vues pour l'entité "domaine"
class DomaineListView(ListView):
    model = Domaine
    template_name = 'domaine_list.html'
    context_object_name = 'domaines'

class DomaineDetailView(DetailView):
    model = Domaine
    template_name = 'domaine_detail.html'
    context_object_name = 'domaine'

class DomaineCreateView(CreateView):
    model = Domaine
    template_name = 'domaine_form.html'
    fields = ['nom']

class DomaineUpdateView(UpdateView):
    model = Domaine
    template_name = 'domaine_form.html'
    fields = ['nom']

class DomaineDeleteView(DeleteView):
    model = Domaine
    template_name = 'domaine_confirm_delete.html'
    success_url = reverse_lazy('domaine_list')
