from django.urls import path
from appfamilia.views import *

urlpatterns = [
    path('inic/', inic, name="coder-inic"),
    path('familias/', familias, name="coder-familias"),
    path('hijos/', hijos, name="coder-hijos"),
    path('representante/', representantes, name="coder-representante"),
    path('entregables/', entregables, name="coder-entregables" )
]
