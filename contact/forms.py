from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom_complet','numero']
        widgets = {
            'nom_complet': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom complet'}),
            'numero': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Entrer numero'})
        }
        labels = {
            'nom_complet':'Nom_complete',
            'numero':'numero',
            
        }
