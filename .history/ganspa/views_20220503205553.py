from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from django.views.generic import TemplateView
from .forms import AccountForm,AddAccountForm

from django.contrib.auth.decorators import login_required

from .models import Account
from .models import Friend
from .forms import HelloForm
from django.shortcuts import redirect


#redirect
@login_required
def top(request):
    return render(request,"Ganspa/top.html")


#各page
def top(request):
    return render(request,"Ganspa/top.html")

def guide(request):
    return render(request,"Ganspa/guide.html")

def users(request):
    return render(request,"Ganspa/users.html")

def user(request):
    return render(request,"Ganspa/user.html")


#registration
class AccountRegistration(TemplateView):

    def __init__(self):
        self.params={
            "AccountCreate":False,
            "account_form":AccountForm(),
            "add_account_form":AddAccountForm(),
        }
    
    def get(self,request):
        self.params["account_form"]=AccountForm()
        self.params["add_account_form"]=AddAccountForm()
        self.params["AccountCreate"]=False
        account=Account.objects.get(user=request.user)
        self.params["account"]=account
        return render(request,"registration/register.html",context=self.params)
    
    def post(self,request):
        self.params["account_form"]=AccountForm(data=request.POST)
        self.params["add_account_form"]=AddAccountForm(data=request.POST)

        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            account=self.params["account_form"].save()
            account.set_password(account.password)
            account.save()
            add_account=self.params["add_account_form"].save(commit=False)
            add_account.user=account

            add_account.save()
            self.params["AccountCreate"]=True
        else:
            print(self.params["account_form"].errors)
        
        return render(request,"registration/register.html",context=self.params)




def users(request):
    data=Account.objects.all()
    params={
        "data": data,
    }

    return render(request,"Ganspa/users.html",params)


