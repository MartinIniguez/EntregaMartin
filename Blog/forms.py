from django import forms
from .models import Post, Autor, Categoria

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'bio', 'email']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'autor', 'categorias']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 10, 'cols': 40}),
            'categorias': forms.CheckboxSelectMultiple(),
        }
        
class BusquedaForm(forms.Form):
    titulo = forms.CharField(label='Buscar por título', max_length=100, required=False)