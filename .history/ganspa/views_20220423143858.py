from django.shortcuts import render
from django.http import HttpResponse

def index(request,id,nickname):
    return HttpResponse("Ganspa")

# Create your views here.
