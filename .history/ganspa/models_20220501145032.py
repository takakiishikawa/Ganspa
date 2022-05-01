from django.db import models
from django.contrib.auth.models import AbstractUser

class Friend(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=200)
    gender=models.BooleanField()
    age=models.IntegerField(default=0)
    birthday=models.DateField()

    def __str__(self):
        return '<Friend:id='+str(self.id)+','+\
            self.name+'('+str(self.age)+')>'

# Create your models here.

class CustomUser(AbstractUser):

    def __str__(self):
        return self.email