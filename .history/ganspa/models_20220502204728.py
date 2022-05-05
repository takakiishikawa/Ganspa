from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    goal=models.CharField(max_length=100)
    coffee=models.BooleanField(max_length=100)



    def __str__(self):
        return self.user.username

# Create your models here.
