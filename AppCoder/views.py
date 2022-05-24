from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Template, Context, loader 
from django.shortcuts import render
from AppCoder.models import *
import datetime 

def curso(request):
    curso = Curso(nombre="Tester", camada="0001")
    curso.save()
    texto = f'---->Curso: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(texto)


# Create your views here.
