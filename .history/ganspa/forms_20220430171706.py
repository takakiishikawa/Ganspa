from django import forms

class GanspaForm(forms.Form):
    forms.choiceField(choices=値,widget=forms.RadioSelect())
