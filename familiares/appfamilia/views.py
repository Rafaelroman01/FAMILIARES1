from django.http import HttpResponse
from appfamilia.models import *
from django.shortcuts import render

def inic(request):
    return render(request, "Appcoder/base.html")

def familias(request):
    return render(request, "Appcoder/familia.html")

def hijos(request):
    return render(request, "Appcoder/hijo.html")

def representantes(request):
    return render(request, "Appcoder/representante.html")

def entregables(request):
    return render(request, "Appcoder/entregable.html")
    

