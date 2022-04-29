from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return render(request,"Ganspa/top.html")

def index2(request):
    return render(request,"Ganspa/guide.html")





# Create your views here.
