from django.urls import path

from . import views
app_name = 'pasteleria'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),
    path('registrar_datos', views.registrar_datos, name='registrar_datos'),
    path('registrocontraseña', views.registrocontraseña, name='registrocontraseña')
]