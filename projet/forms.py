from django import forms
from projet.models import Repertoire


#there we are going to create one formulare by instance the class Repository
class RepertoireForm(forms.ModelForm):
    class Meta:
        model = Repertoire
        fields = ['nom_repertoire']
        widgets = {
            'nom_repertoire': forms.TextInput(attrs={'class':'form-control form-is_valid', 'placeholder':'Nom de repertoire'})
        }
        labels = {
            'nom_repertoire':'Nom repertoire',
            
        }


