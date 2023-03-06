# Tienda
Proyecto Django

## Creación FORM MODEL "ARTICULO"

[Models forms][https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/]

Le añado articulos nuevos y pruebo a insertar una imagen, para ello es necesario descargar la libreria pillow

```pip install pillow```

Para crear un Form model en Django con una clase Articulo en models.py, una clase ArticuloForm en forms.py y un método altarticulo en views.py, puedes seguir estos pasos:

1-En models.py, define la clase Articulo con los atributos name, stock, pvp e imagen, utilizando los campos adecuados de Django
```
from django.db import models

class Articulo(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    pvp = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to='articulos') 

```

2-En forms.py, define la clase ArticuloForm como un formulario de modelo que utiliza la clase Articulo:


```
from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['name', 'stock', 'pvp', 'imagen']

```

3-Crear la vista altaArticulo en "views.py" que maneje la creación de un nuevo articulo a traves de ArticuloForm:


```
def Altaarticulo(request):
    if request.method == 'POST':
        form=ArticuloForm(request.POST,request.FILES)
        if form.is_valid():
            print("fromulario validado correctamente")
            form.save()
            return redirect('inicio')
        else:
            form=ArticuloForm()
            return render(request,'tienda/prueba2.html',{"form":form})
```
