from django.shortcuts import render
from django.http import HttpResponse
from .forms import GanspaForm

def top(request):
    msg=request.POST["msg"]
    params={
        "msg":"おはようございます,"+msg+"さん",
        "form":GanspaForm()
    }

    return render(request,"Ganspa/top.html",params)

def guide(request):
    return render(request,"Ganspa/guide.html")

def users(request):
    return render(request,"Ganspa/users.html")

def user(request):
    return render(request,"Ganspa/user.html")

def login(request):
    return render(request,"Ganspa/login.html")

def register(request):
    params={
        "title":"Ganspa",
        "msg":"お名前は?",
    }
    return render(request,"Ganspa/register.html")



# Create your views here.
