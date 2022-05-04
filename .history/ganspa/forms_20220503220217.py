from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model=User
        fields=('username','password',)
        labels={'username':"ユーザーID","password":"パスワード"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        model=Account
        fields={'goal','coffee','job','job1',}
        labels={'goal':'Ganspaのゴール','coffee':'コーヒーはお好きですか？','job':'職業','job1':'職業1',}


class HelloForm(forms.Form):
    name=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':'form-control'}))
    mail=forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender=forms.BooleanField(label='Gender',required=False,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age=forms.IntegerField(label='Age',widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday=forms.DateField(label='Birth',required=False,widget=forms.DateInput(attrs={'class':'form-control'}))
