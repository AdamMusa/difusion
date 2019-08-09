from django.db import models
from projet.models import Repertoire

# Create your models here.

class Contact(models.Model):
    nom_complet = models.CharField(max_length = 100)
    numero = models.CharField(max_length = 14)
    repertoire=models.ForeignKey(Repertoire,on_delete=models.CASCADE, related_name='contacts')