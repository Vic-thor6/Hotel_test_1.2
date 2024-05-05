from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienesomos/', views.quienesomos, name='quienesomos'),
    path('calzado/', views.calzado, name='calzado'),
    path('registrar_cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
]
