from django.db import models
from projet.models import Repertoire
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    content = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    repertoire=models.ForeignKey(Repertoire,on_delete=models.CASCADE)

    def __str__(self):
        return self.repertoire.nom_repertoire