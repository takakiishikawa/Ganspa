from django.shortcuts import render
from django.http import HttpResponse
from .forms import GanspaForm

def top(request):
    msg=request.POST['msg']
    params={
        'msg':'おはようございます,'+msg+'さん',
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
        "message":"your data:",
        "Form":GanspaForm()
    }
    if(request.method=='POST'):
        params['message']='名前:'+request.POST['name']+\
            '<br>メール:'+request.POST['mail']+\
            '<br>年齢:'+request.POST['age']
        params['form']=GanspaForm(request.POST)
    return render(request,"Ganspa/register.html",params)



# Create your views here.
