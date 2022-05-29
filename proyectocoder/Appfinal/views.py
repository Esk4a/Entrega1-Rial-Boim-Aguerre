from urllib import request
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
from django.template import loader
from Appfinal.models import Peliculas, Sucursales, Contactos
from Appfinal.forms import *
import datetime

def index(request):
    return render(request, "Appfinal/index.html")

def Movies(request):
    Movies = Peliculas.objects.all()

    context_dict = {
        'Movie': Movies
    }

    return render(
        request=request,
        context=context_dict,
        template_name="Appfinal/Peliculas.html"
    )

def PeliculasForm(request):
    if request.method == 'POST':
        peliculas = PeliculasFormulario(request.POST)
        print(peliculas)

        if peliculas.is_valid:
            info = peliculas.cleaned_data
            movie = Peliculas (titulo = info['titulo'], 
            duracion = info['duracion'],
            emision = info['emision'])

            movie.save()
            Movies = Peliculas.objects.all()
            context_dict = {'Movie': Movies}
    
            return render(
             request=request,
             context=context_dict,
             template_name="Appfinal/Peliculas.html")
    else:
        peliculas = PeliculasFormulario()
    return render(request, "Appfinal/PeliculasFormulario.html", {"peliculas":peliculas})


def Sucursal(request):
    Sucursal = Sucursales.objects.all()

    context_dict = {
        'Places': Sucursal
    }

    return render(
        request=request,
        context=context_dict,
        template_name="Appfinal/Sucursales.html"
    )

def SucursalesForm(request):
    if request.method == 'POST':
        sucursales= SucursalesFormulario(request.POST)
        print(sucursales)

        if sucursales.is_valid:
            info = sucursales.cleaned_data
            place = Sucursales (ciudad = info['ciudad'], 
            calle = info['calle'],
            altura = info['altura'])

            place.save()
            Sucursal = Sucursales.objects.all()
            context_dict = {'Places': Sucursal}

            return render(
             request=request,
             context=context_dict,
             template_name="Appfinal/Sucursales.html")
    else:
        sucursales = SucursalesFormulario()
    return render(request, "Appfinal/SucursalesFormulario.html", {"sucursales":sucursales})

def Contacto(request):
    Contacto = Contactos.objects.all()

    context_dict = {
        'social': Contacto
    }

    return render(
        request=request,
        context=context_dict,
        template_name="Appfinal/Contactos.html"
    )

def ContactosForm(request):
    if request.method == 'POST':
       contactos= ContactosFormulario(request.POST)
       print(contactos)

       if contactos.is_valid:
            info = contactos.cleaned_data
            Redes = Contactos (social = info['social'], 
            Telefono = info['Telefono'])

            Redes.save()
            Contacto = Contactos.objects.all()
            context_dict = {'social': Contacto}

            return render(
                request=request,
                context=context_dict,
                template_name="Appfinal/Contactos.html")
    else:
        contactos = ContactosFormulario()
    return render(request, "Appfinal/ContactosFormulario.html", {"contactos":contactos})


def Search(request):
    context_dict = dict()
    if request.GET['titulo_search']:
        search_param = request.GET['titulo_search']
        Movies = Peliculas.objects.filter(titulo__contains=search_param)
        context_dict = {
            'Movie': Movies
        }    

    return render(
        request=request,
        context=context_dict,
        template_name="Appfinal/Peliculas.html",
    )
