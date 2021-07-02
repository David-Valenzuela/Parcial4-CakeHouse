from django.urls import path

from . import views
app_name = 'pasteleria'
urlpatterns = [
    path('', views.menu, name='menu'),
    path('agregar_cliente', views.agregar_cliente, name='agregar_cliente'),
    path('registrar_datos', views.registrar_datos, name='registrar_datos'),
    path('registro_clave', views.registro_clave, name='registro_clave'),

    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
]