from django.urls import path

from Appfinal import views


app_name='Appfinal'
urlpatterns = [
    path('', views.index, name='Index'),
    path('Peliculas/', views.Movies, name='Peliculas'),
    path('Sucursales/', views.Sucursal, name='Sucursales'),
    path('Contactos/', views.Contacto, name='Contactos'),
    path('PeliculasFormulario/', views.PeliculasForm, name='PeliculasFormulario'),
    path('SucursalesFormulario/', views.SucursalesForm, name='SucursalesFormulario'),
    path('ContactosFormulario/', views.ContactosForm, name='ContactosFormulario'),
    path('Search/', views.Search, name='Search'),



]