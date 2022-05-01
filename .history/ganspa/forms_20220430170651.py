from django import forms

class GanspaForm(forms.Form):
    check=forms.BooleanField(label='Checkbox',required=False)
