from datetime import time
from django import http
from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from pasteleria.models import Ciudad, Cliente, Comuna, Producto
from django.utils import timezone
from django.urls import reverse


def index(request):
    return render(request,'pasteleria/index.html')

def agregar_cliente(request):
    listado_comuna = Comuna.objects.all()
    listado_ciudad = Ciudad.objects.all()
    context = {'comunas':listado_comuna,'ciudades':listado_ciudad}
    return render(request,'pasteleria/agregar_cliente.html',context)

def registrar_datos(request):
    listado_comuna = Comuna.objects.all()
    listado_ciudad = Ciudad.objects.all()
    listado_cliente = Cliente.objects.all()
    estado = True

    if request.POST['run'].strip() != "":
        run = request.POST['run'].strip()
    else:
         return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})    
    
    if request.POST['nombre'].strip() != "":
        nombre = request.POST['nombre'].strip()
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})   

    if request.POST['paterno'].strip() != "":
        paterno = request.POST['paterno'].strip()
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})   

    if request.POST['materno'].strip() != "":
        materno = request.POST['materno'].strip()
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})   
    
    if request.POST['email'].strip() != "":
        email = request.POST['email'].strip()
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})   

    if request.POST['celular'].strip() != "":
        celular = request.POST['celular'].strip()
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})   

    if request.POST['direccion'].strip() != "":
        direccion = request.POST['direccion'].strip()
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})           
    
    if request.POST['numeracion'].strip() != "":
        num = request.POST['numeracion'].strip()
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})    
    
    if request.POST['ciudad'] != "":
        id_ciudad = request.POST['ciudad']
        if request.POST['comuna'] != "":
            id_comuna = request.POST['comuna']
        else:
            return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})   
    else:
        return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "No pueden haber campos vacios",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad}) 

    ciudad = Ciudad.objects.get(pk = request.POST['ciudad'])
    comuna = Comuna.objects.get(pk = request.POST['comuna'])
    
    for c in listado_cliente:
        if run == c.run_cliente:
            estado = False   
            return render(request, 'pasteleria/agregar_cliente.html', {
            'error_message': "Cliente ya ingresado",
            'comunas':listado_comuna,
            'ciudades':listado_ciudad})   
    if estado == True:
        carrito = {'run':run,'nombre':nombre,'ap_paterno':paterno,'ap_materno':materno,'email':email,'celular':celular,'direccion':direccion,'numeracion':num,'comuna':comuna, 'ciudad':ciudad,'id_ciudad':id_ciudad,'id_comuna':id_comuna}
        return render(request,'pasteleria/password_cliente.html',carrito)