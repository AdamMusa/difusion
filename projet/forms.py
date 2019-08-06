from django import forms
from projet.models import Repertoire



class RepertoireForm(forms.ModelForm):
    class Meta:
        model = Repertoire
        fields = ['nom_repertoire']
        widgets = {
            'nom_repertoire': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom de repertoire'})
        }
        labels = {
            'nom_repertoire':'Nom repertoire',
            
        }