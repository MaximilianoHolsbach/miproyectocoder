from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Template, Context, loader 
from django.shortcuts import render
from AppCoder.forms import *
from AppCoder.models import *
import datetime 

def index(request):
   return render(request, "AppCoder/index.html")
   


# Create your views here.
