from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from projet.models import Repertoire
from projet.forms import RepertoireForm

class RepertoireCreateView(CreateView):
 
    form_class = RepertoireForm
    template_name = 'projet/index.html'
    success_url = reverse_lazy('projet:list')

class RepertoireListView(ListView):
    model = Repertoire
    template_name = 'projet/list.html'
    context_object_name = 'users'

class RepertoireUpdateView(UpdateView):
    form_class = RepertoireForm
    template_name = 'projet/index.html'
    success_url = reverse_lazy('projet:list')
    model = Repertoire

class RepertoireDeleteView(DeleteView):
    model = Repertoire
    template_name = 'projet/delete_confirm.html'
    context_object_name = 'user'
    success_url = reverse_lazy('projet:list')
