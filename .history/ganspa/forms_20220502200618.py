from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model=User
        fields=('username','email','password')
        labels={'username':"ユーザー名","email":"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        model=Account
        fields={'last_name','first_name',}
        labels={'last_name':'苗字','first_name':'名前',}