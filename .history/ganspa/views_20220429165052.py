from django.shortcuts import render
from django.http import HttpResponse
from .models import Friend

def index1(request):
    return render(request,"Ganspa/top.html")

def index2(request):
    return render(request,"Ganspa/guide.html")




# Create your views here.
