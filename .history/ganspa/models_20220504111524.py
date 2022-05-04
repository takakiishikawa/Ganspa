from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):

    user=models.OneToOneField(User,on_delete=models.CASCADE)

    goal=models.CharField(max_length=100)
    coffee=models.BooleanField(max_length=100)
    job=models.CharField(max_length=100)



    def __str__(self):
        return self.user.username

class Friend(models.Model):
    name=models.CharField(max_length=100)
    mail=models.EmailField(max_length=200)
    gender=models.BooleanField()
    age=models.IntegerField(default=0)
    birthday=models.DateField()

    def __str__(self):
        return '<Friend:id='+str(self.id)+self.name+str(self.age)+'>'
        
