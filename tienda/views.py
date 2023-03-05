from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from tienda.forms import NameForm
from tienda.forms import ArticuloForm
# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request,
    'tienda/post/list.html',
    {'posts': posts})

def post_detail(request,id):
   # try:
     #   posts = Post.published.get(id=id)
    #except Post.DoesNotExist:
       # raise Http404("No post found")
    post = get_object_or_404(Post,
                            id=id,
                            status=Post.Status.PUBLISHED)
    return render(request,
        'tienda/post/list.html',
            {'posts': post})

def prueba(request):
     if request.method == 'POST':
         form = NameForm(request.POST)
         if form.is_valid():
            print(form.cleaned_data["nombre"])
         return render(request,'tienda/prueba.html',{'msg':"Formulario recibido"})
     else:
        form=NameForm()
        return render(request,'tienda/prueba.html',{'form':form})
def Altaarticulo(request):
    if request.method == 'POST':
        form=ArticuloForm(request.POST)
        if form.is_valid():
            print("fromulario validado correctamente")
            form.save()
        else:
            form=ArticuloForm()
            return render(request,'tienda/prueba2.html',{"form":form})
