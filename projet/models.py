from django.db import models
from django.contrib.auth.models import User
import datetime

class Repertoire(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    nom_repertoire = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now = False,auto_now_add = True)

    def __str__(self):
        return self.nom_repertoire

class Message(models.Model):
    content = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    repertoire=models.ForeignKey(Repertoire,on_delete=models.CASCADE)

    def __str__(self):
        return self.repertoire.nom_repertoire

class Contact(models.Model):
    nom_complet = models.CharField(max_length = 50)
    numero = models.CharField(max_length = 14)
    repertoire=models.ForeignKey(Repertoire,on_delete=models.CASCADE)
    