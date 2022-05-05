from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model=User
        fields=('username','password')
        labels={'username':"ユーザー名","password":"パスワード"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        model=Account
        fields={"first_name","last_name",'goal','coffee',}
        labels={"first_name":"名前","last_name":"苗字",'coffee':'コーヒーはお好きですか？','goal':'Ganspaのゴール',}