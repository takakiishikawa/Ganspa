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
        fields={'coffee','first_name',}
        labels={'coffee':'コーヒー','first_name':'名前',}