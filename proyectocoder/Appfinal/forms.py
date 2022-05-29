import datetime
from django import forms
from django.forms import ModelForm
#from Appfinal.models import *


class PeliculasFormulario(forms.Form):

    titulo = forms.CharField(max_length=40)
    duracion = forms.IntegerField()
    emision = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

class SucursalesFormulario(forms.Form):

    ciudad = forms.CharField(max_length=40)
    calle = forms.CharField(max_length=40)
    altura = forms.IntegerField()

class ContactosFormulario(forms.Form):
    social = forms.CharField(max_length=40)
    Telefono = forms.IntegerField()
    