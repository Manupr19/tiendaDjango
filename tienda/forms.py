from django import forms
from .models import Articulo

class NameForm(forms.Form):
    nombre = forms.CharField(label='Your name', max_length=100)
class ArticuloForm(forms.ModelForm):
    class Meta:
        model= Articulo 
        fields=['name','stock','pvp','imagen']
    
