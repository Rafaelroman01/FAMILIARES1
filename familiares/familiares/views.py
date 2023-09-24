from django.http import HttpResponse



def vista_saludo(request):
    return HttpResponse("Bienvenidos")
    