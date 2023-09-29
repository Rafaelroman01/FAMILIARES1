from django.urls import path
from appfamilia.views import *

urlpatterns = [
    path('inic/', inic),
    path('familias/', familias),
    path('hijos/', hijos),
    path('padres/', padres),
    path('entregables/', entregables)
]
