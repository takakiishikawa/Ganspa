from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"Ganspa/top.html")

# Create your views here.
