from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from projet.models import Repertoire
from projet.forms import RepertoireForm


#now we create a repository
class RepertoireCreateView(CreateView):
    #projet = projet_repertoire.user_id
    form_class = RepertoireForm
    template_name = 'projet/index.html'
    success_url = reverse_lazy('projet:list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#we are listing all the repository
class RepertoireListView(ListView):
    model = Repertoire
    template_name = 'projet/list.html'
    context_object_name = 'repertoires'
#we are going to update one repository
class RepertoireUpdateView(UpdateView):
    form_class = RepertoireForm
    template_name = 'projet/index.html'
    success_url = reverse_lazy('projet:list')
    model = Repertoire
# end we are going to delete one repository
class RepertoireDeleteView(DeleteView):
    model = Repertoire
    template_name = 'projet/delete_confirm.html'
    context_object_name = 'user'
    success_url = reverse_lazy('projet:list')
