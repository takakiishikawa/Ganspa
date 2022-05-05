from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):


    last_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

# Create your models here.
