from django.http import HttpResponse
from appfamilia.models import *

def saludo(request):
    return HttpResponse("Estas en el inicio")

def familias(request):
    return HttpResponse("Estas en vista familias")

def hijos(request):
    return HttpResponse("Estas en vista hijos")

def padres(request):
    return HttpResponse("Estas en vista padres")

def entregables(request):
    return HttpResponse("Estas en vista entregables")
    

