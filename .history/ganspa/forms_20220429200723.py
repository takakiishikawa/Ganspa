from django import forms

class GanspaForm(forms.Form):
    name=forms.CharField(label="name")
    password=forms.CharField(label="password")
    age=forms.IntegerField(label="age")
