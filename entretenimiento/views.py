from django.shortcuts import redirect, render
from .models import VideoJuegos, Peliculas, Series
from .forms import VideoJuegosForm, PeliculasForm, SeriesForm, VideoJuegosBusqueda
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

def videojuego(request):
    return render(request, 'entretenimiento/videojuego.html', {})

@login_required
def crear_videojuego(request):
    
    if request.method == 'POST':
        form = VideoJuegosForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            videojuego = VideoJuegos(nombre=data['nombre'], genero=data['genero'], divertido=data['divertido'])
            videojuego.save()
            return redirect('index')
        
    context = {'form': VideoJuegosForm}
    return render(request, 'entretenimiento/crear_videojuego.html', context)

def lista_videojuegos(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        videojuegos = VideoJuegos.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        videojuegos = VideoJuegos.objects.all()
    
    form = VideoJuegosBusqueda()
    return render(request, 'entretenimiento/lista_videojuegos.html', {'form': form, 'videojuegos': videojuegos})


class DetalleVideojuego(DetailView):
    model = VideoJuegos
    template_name = 'entretenimiento/detalle_videojuego.html'
    
class EditarVideojuego(UpdateView):
    model = VideoJuegos
    success_url = '/entretenimiento/videojuegos/lista'
    fields = ['nombre', 'genero', 'divertido']

class BorrarVideojuego(DeleteView):
    model = VideoJuegos
    success_url = '/entretenimiento/videojuegos/lista'



def pelicula(request):
    return render(request, 'entretenimiento/pelicula.html', {})

@login_required
def crear_pelicula(request):
    
    if request.method == 'POST':
        form = PeliculasForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            pelicula = Peliculas(nombre=data['nombre'], categoria=data['categoria'], divertida=data['divertida'])
            pelicula.save()
            return redirect('index')
        
    context = {'form': PeliculasForm}
    return render(request, 'entretenimiento/crear_pelicula.html', context)


def serie(request):
    return render(request, 'entretenimiento/serie.html', {})

@login_required
def crear_serie(request):
    
    if request.method == 'POST':
        form = SeriesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            serie = Series(nombre=data['nombre'], categoria=data['categoria'], divertida=data['divertida'])
            serie.save()
            return redirect('index')
        
    context = {'form': SeriesForm}
    return render(request, 'entretenimiento/crear_serie.html', context)