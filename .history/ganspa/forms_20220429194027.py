from django import forms

class GanspaForm(forms.form):
    name=forms.CharField(label="name")
    mail=forms.CharField(label="mail")
    age=forms.IntegerField(label="age")
    