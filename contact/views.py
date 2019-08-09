from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from contact.models import Contact
from projet.models import Repertoire
from django.contrib.auth.models import User
from contact.forms import ContactForm

# Create your views here.
class ContactCreateView(CreateView):
    #contact = contact_repertoire.user_ids
    form_class = ContactForm
    template_name = 'contact/create.html'
    # success_url = reverse_lazy('repertoire:list', {'pk': sel})
    repertoire_id = None

    def get_success_url(self):
        success_url = reverse_lazy('repertoire:list', kwargs = {'pk': self.repertoire_id})
        print(success_url)
        return success_url

    def form_valid(self, form):
        repertoire = get_object_or_404(Repertoire, pk=self.repertoire_id)
        form.instance.repertoire= repertoire
        print(form)

        return super().form_valid(form)


#we are listing all the contact you have
class ContactListView(ListView):
    model = Contact
    template_name = 'contact/list.html'
    context_object_name = 'users'


#we are going to update one contact 
class ContactUpdateView(UpdateView):
    form_class = ContactForm
    template_name = 'contact/create.html'
    success_url = reverse_lazy('contact:list')
    model = Contact

# end we are going to delete one contact
class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'contact/delete_confirm.html'
    context_object_name = 'user'
    success_url = reverse_lazy('contact:list')


class RepertoireDetailView(DetailView):
    model = Repertoire
    template_name = 'contact/list.html'
    context_object_name = 'repertoire'
