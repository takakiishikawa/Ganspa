from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index(request):
    data=Friend.objects.all()
    params={
        "title":"Ganspa",
        "message":"all friends.",
        "data":data,
    }
    return render(request,"Ganspa/top.html")

# Create your views here.
