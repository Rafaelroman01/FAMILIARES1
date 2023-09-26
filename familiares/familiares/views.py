from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime



def vista_saludo(request):
    return HttpResponse("Bienvenidos")

def vista_plantilla(request):
    #Abrimos el archivo
    archivo = open(r"\Users\Familia\Desktop\Carpeta VSC\Familiares1\familiares\familiares\templates\inicio.html")
    #Creamos el objeto plantilla
    plantilla = Template(archivo.read())
    # Cerramos el archivo para liberar recursos
    archivo.close()
    #Diccionario con Datos para la plantilla
    datos = {"nombre": "Rafael", "fecha": datetime.now(), "apellido": "Roman", "edad": [24,43,54]}
    #Creamos el contexto 
    contexto = Context(datos)
    #Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)
    #Retornamos la respuesta
    return HttpResponse(documento)

def vista_familiares(request):
    #Abrimos el archivo
    archivo = open(r"\Users\Familia\Desktop\Carpeta VSC\Familiares1\familiares\familiares\templates\listado_familiares.html")
    #Creamos el objeto plantilla
    plantilla = Template(archivo.read())
    # Cerramos el archivo para liberar recursos
    archivo.close()
    #Diccionario con Datos para la plantilla
    listado_familiares = ["Carlos Ramirez", "Jose Ramirez", "Maria Ramirez", "Eloiza Ramirez", "Marcos Ramirez", "Matea Ramirez"]
    datos = {"familiares": "cercanos", "listado_familiares": listado_familiares}
    #Creamos el contexto 
    contexto = Context(datos)
    #Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)
    #Retornamos la respuesta
    return HttpResponse(documento)

def vista_for(request):
    #Abrimos el archivo
    archivo = open(r"\Users\Familia\Desktop\Carpeta VSC\Familiares1\familiares\familiares\templates\listadofor_familiares.html")
    #Creamos el objeto plantilla
    plantilla = Template(archivo.read())
    # Cerramos el archivo para liberar recursos
    archivo.close()
    #Diccionario con Datos para la plantilla
    listado_familiares = ["Carlos Ramirez", "Jose Ramirez", "Maria Ramirez", "Eloiza Ramirez", "Marcos Ramirez", "Matea Ramirez"]
    datos = {"familiares": "cercanos", "listado_familiares": listado_familiares}
    #Creamos el contexto 
    contexto = Context(datos)
    #Renderizamos la plantilla para crear la respuesta
    documento = plantilla.render(contexto)
    #Retornamos la respuesta
    return HttpResponse(documento)

def vista_familiares2(request):
    #Diccionario con Datos para la plantilla
    listado_familiares = ["Carlos Ramirez", "Jose Ramirez", "Maria Ramirez", "Eloiza Ramirez", "Marcos Ramirez", "Matea Ramirez"]
    datos = {"familiares": "cercanos", "listado_familiares": listado_familiares}
    plantilla = loader.get_template("listadofamiiares2.html")
    documento = plantilla.render(datos)
    return HttpResponse(documento)
    

