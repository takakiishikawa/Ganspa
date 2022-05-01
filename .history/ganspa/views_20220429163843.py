from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index1(request):
    data=Friend.objects.all()
    params={
        "title":"Ganspa",
        "message":"all friends.",
        "data":data,
    }
    return render(request,"Ganspa/top.html",params)

def index2(request):
    return render(request,"Ganspa/guide.html")




# Create your views here.
