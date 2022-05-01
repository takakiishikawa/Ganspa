from django import forms

class GanspaForm(forms.Form):
    data=[
        ("one","radio 1"),
        ("two","radio 2"),
        ("three","radio 3"),
    ]
    choice=forms.ChoiceField(label='radio',\
        choices=data,widget=forms.RadioSelect())