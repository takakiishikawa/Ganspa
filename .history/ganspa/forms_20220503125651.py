from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model=User
        fields=('username','password')
        labels={'username':"ユーザーID","password":"パスワード"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        model=Account
        fields={'name','job','coffee','coffee_like','goal'}
        labels={"name":"お名前",'coffee':'コーヒーはお好きですか？','goal':'Ganspaのゴール','coffee_like':'好きなコーヒー','job':'職業'}