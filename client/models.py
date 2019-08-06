from django.db import models
from django.contrib.auth.models import User


class Credit(models.Model):
    credit = models.IntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.credit
    
