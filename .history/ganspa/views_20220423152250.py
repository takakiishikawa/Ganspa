from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    params={
        "title":"takaki",
        "msg":"takaki",
    }
    return render(request,"Ganspa.top/html",params)

# Create your views here.
