from django import forms

class NameForm(forms.Form):
    nombre = forms.CharField(label='Your name', max_length=100)
    