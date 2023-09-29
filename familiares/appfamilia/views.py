from django.http import HttpResponse
from appfamilia.models import *
from django.shortcuts import render

def inic(request):
    return render(request, "Appcoder/index.html")

def familias(request):
    return HttpResponse("Estas en vista familias")

def hijos(request):
    return HttpResponse("Estas en vista hijos")

def padres(request):
    return HttpResponse("Estas en vista padres")

def entregables(request):
    return HttpResponse("Estas en vista entregables")
    

