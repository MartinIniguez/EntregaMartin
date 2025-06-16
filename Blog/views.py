from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm
from .models import Post


# Create your views here.

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Blog/autor_creado.html', {'form': form})
    else:
        form = AutorForm()
    return render(request, 'Blog/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Blog/categoria_creada.html', {'form': form})
    else:
        form = CategoriaForm()
    return render(request, 'Blog/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'Blog/post_creado.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'Blog/crear_post.html', {'form': form})

def buscar_post(request):
    form = BusquedaForm(request.GET or None)
    posts = Post.objects.all()

    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        if titulo:
            posts = posts.filter(titulo__icontains=titulo)

    return render(request, 'Blog/buscar_post.html', {'form': form, 'posts': posts})

def index(request):
    context = {"mensaje": "Bienvenido a Mi Blog"} 
    return render(request, 'Blog/index.html', context)
