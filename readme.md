# Tienda
Proyecto Django

## Creación clase Articulo en models.py

[Models forms][https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/]

Le añado articulos nuevos y pruebo a insertar una imagen, para ello es necesario descargar la libreria pillow
```pip install pillow```
Despues en models.py añado los nuevos atributos, en este caso es el de imagen 
```imagen= models.ImageField(upload_to='/tienda')```
De esta forma especifico que coja la imagen cargada desde el directorio /tienda
Posteriormente me voy a Views.py y creo Altaarticulo para tratar la petición GET y crear el formulario o la POST para guardarlo 