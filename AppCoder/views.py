from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso #Agregar datos a la base desde view


# Create your views here.

def curso(self):

    curso = Curso (nombre="Desarrollo web", comision="31310")
    curso.save()

    Texto = f"Curso: {curso.nombre} Comision: {curso.comision}"

    return HttpResponse(Texto)