from django.http import HttpResponse
from appfamilia.models import *
from django.shortcuts import render
from appfamilia.forms import *

def inic(request):
    return render(request, "Appcoder/base.html")

def familias(request):
    return render(request, "Appcoder/familia.html")

def creacion_familia(request):
    if request.method == "POST":
        nombre_nombre = request.POST["nombre"]
        numero_camada = request.POST["camada"]
        nombre = Familia(nombre=nombre_nombre, camada=numero_camada)
        nombre.save()
    
    return render(request, "Appcoder/familias_formulario.html")
        
def hijos(request):
    return render(request, "Appcoder/hijo.html")

def creacion_hijos(request):
    if request.method == "POST":
        formulario = HijoFormulario(request.POST)
        #Validamos que el formulario no tenga problemas
        if formulario.is_valid():
            #Recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data
            hijo = Hijo(nombre=data["nombre"], apellido=data["apellido"], email=data["email"] )
            hijo.save()
        pass
        
    
    formulario = HijoFormulario()
    contexto ={"formulario":formulario}
    
    return render(request, "Appcoder/hijo_formularios.html", contexto)

def representantes(request):
    return render(request, "Appcoder/representante.html")

def entregables(request):
    return render(request, "Appcoder/entregable.html")
    

