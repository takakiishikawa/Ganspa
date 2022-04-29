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




# Create your views here.
