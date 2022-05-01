from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return render(request,"Ganspa/top.html")

def guide(request):
    return render(request,"Ganspa/guide.html")

def users(request):
    return render(request,"Ganspa/users.html")

def user(request):
    return render(request,"Ganspa/user.html")

def login(request):
    return render(request,"Ganspa/login.html")

def register(request):
    return render(request,"Ganspa/register.html")


# Create your views here.
