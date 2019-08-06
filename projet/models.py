from django.db import models
from django.contrib.auth.models import User
import datetime

class Repertoire(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    nom_repertoire = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now = False,auto_now_add = True)

    def __str__(self):
        return self.nom_repertoire