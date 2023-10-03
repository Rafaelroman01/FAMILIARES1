from django.urls import path
from appfamilia.views import *

urlpatterns = [
    path('inic/', inic, name="coder-inic"),
    path('familias/', familias, name="coder-familias"),
    path('familias/crear/', creacion_familia, name="coder-familias-crear"),
    path('hijos/', hijos, name="coder-hijos"),
    path('hijos/crear/', creacion_hijos, name="coder-hijos-crear"),
    path('representante/', representantes, name="coder-representante"),
    path('entregables/', entregables, name="coder-entregables" )
]
