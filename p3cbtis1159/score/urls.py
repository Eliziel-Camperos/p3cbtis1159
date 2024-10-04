from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("Eliziel/",views.Eliziel,name="Eliziel"),
    path("minovia/",views.minovia,name="minovia"),
    path("contactos/",views.contactos,name="contactos"),
    path("empleados/",views.empleados,name="empleados"),
    path("Mercancia/",views.Mercancia,name="Mercancia"),
    path("Comics/",views.Comics,name="Comics"),
    path("Ventas/",views.Ventas,name="Ventas"),
]