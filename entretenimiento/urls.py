from django.urls import path
from . import views

urlpatterns = [
    path('videojuego/', views.videojuego, name='videojuego'),
    path('videojuegos/crear',views.crear_videojuego, name='crear_videojuego'),
    path('videojuegos/lista', views.lista_videojuegos, name='lista_videojuegos'),
    path('videojuegos/<int:pk>', views.DetalleVideojuego.as_view() , name='detalle_videojuego'),
    path('videojuegos/<int:pk>/editar', views.EditarVideojuego.as_view() , name='editar_videojuego'),
    path('videojuegos/<int:pk>/borrar', views.BorrarVideojuego.as_view() , name='borrar_videojuego'),
    path('pelicula/', views.pelicula, name='pelicula'),
    path('peliculas/crear', views.crear_pelicula, name='crear_pelicula'),
    path('serie/', views.serie, name='serie'),
    path('series/crear', views.crear_serie, name='crear_serie'),
]
