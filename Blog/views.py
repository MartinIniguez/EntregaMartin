from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from .models import Post


# Create your views here.

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'Blog/crear_autor.html', {'form': form})
    
def crear_categoria(request):
   form = CategoriaForm(request.POST or None)
   if form.is_valid():
       form.save()
       return render(request, 'Blog/crear_categoria.html', {'form': form})
   
   
def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'Blog/crear_post.html', {'form': form})
    
    
def buscar_post(request):
    resultado  = None
    form = BusquedaPostForm(request.GET or None)
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        resultado = Post.objects.filter(titulo__icontains=titulo)
    return render(request, 'Blog/buscar_post.html', {'form': form, 'resultado': resultado})

def index(request):
    context = {"mensaje": "Bienvenido a Mi Blog"} 
    return render(request, 'Blog/index.html', context)
