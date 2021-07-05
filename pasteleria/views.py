from datetime import time
from django import http
from django.shortcuts import render
from django.http import HttpResponse, response, HttpResponseRedirect
from pasteleria.models import Ciudad, Cliente, Comuna, Producto, Pago
from django.contrib.auth.models import Permission, User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


#MENU PRINCIPAL
def menu(request):
    if request.user.is_authenticated:
        listado_producto = Producto.objects.all()
        context = {'listado_producto':listado_producto,'sesion':'Cerrar sesión'}
        return render(request,'pasteleria/menu.html',context)
    else:
        listado_producto = Producto.objects.all()
        context = {'listado_producto':listado_producto}
        return render(request,'pasteleria/menu.html',context)

def menu_denegado(request):
    logout(request)
    listado_producto = Producto.objects.all()
    context = {'listado_producto':listado_producto}
    return render(request,'pasteleria/menu.html',context)


#AGRERGAR CLIENTE
def agregar_cliente(request):
    listado_comuna = Comuna.objects.all()
    listado_ciudad = Ciudad.objects.all()
    context = {'comunas':listado_comuna,'ciudades':listado_ciudad}
    return render(request,'pasteleria/agregar_cliente.html',context)

#REGISTRAR DATOS DEL CLIENTE
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
        return render(request,'pasteleria/registro_clave.html',carrito)


#Registro Contraseña
def registro_clave(request):
    run = request.POST['run']
    nombre = request.POST['nombre']
    paterno = request.POST['paterno']
    materno = request.POST['materno']
    email = request.POST['email']
    celular = request.POST['celular']
    direccion = request.POST['direccion']
    num = request.POST['numeracion']
    id_ciudad = request.POST['ciudad']
    id_comuna = request.POST['comuna']
    ciudad = Ciudad.objects.get(pk = request.POST['ciudad'])
    comuna = Comuna.objects.get(pk = request.POST['comuna'])
    context = {'error':"Contraseña incorrecta, debe tener minimo 6 caracteres y maximo 12.",'error_password':"Ambas contraseñas deben ser iguales.",'run':run,'nombre':nombre,'ap_paterno':paterno,'ap_materno':materno,'email':email,'celular':celular,'direccion':direccion,'numeracion':num,'comuna':comuna, 'ciudad':ciudad,'id_ciudad':id_ciudad,'id_comuna':id_comuna}

    if request.POST['password'].strip() != "":
        password1 = request.POST['password']
        password2 = request.POST['password2']
    else:
        return render(request, 'pasteleria/registro_clave.html', context) 

    caracters_pass = len(password1)

    ciu = Ciudad.objects.get(id = id_ciudad)
    com = Comuna.objects.get(id = id_comuna)
    fecha_hora = timezone.now()

    cliente = Cliente(run_cliente = run, nombre = nombre, ap_paterno = paterno, ap_materno = materno, 
                    email = email, celular = celular, direccion = direccion, numeracion = num, password = password1 ,fecha_cliente = fecha_hora)
    cliente.comuna = com
    cliente.ciudad = ciu

    if caracters_pass <= 12:
        if caracters_pass >= 6:    
            if password1 != password2:
                return render(request, 'pasteleria/registro_clave.html',context) 
            else:
                cliente.save()
                permiso1 = Permission.objects.get(name='Es comprador')
                permiso2 = Permission.objects.get(name='Can view producto')
                user = User.objects.create_user(run,email,password1)
                user.first_name = nombre
                user.last_name = paterno
                user.user_permissions.add(permiso1,permiso2)
                user.is_staff = True
                user.save()
                return HttpResponseRedirect(reverse('pasteleria:iniciar_sesion'))
        else:
            cliente.save()
            permiso1 = Permission.objects.get(name='Es comprador')
            permiso2 = Permission.objects.get(name='Can view producto')   
            user = User.objects.create_user(run,email,password1)
            user.first_name = nombre
            user.last_name = paterno
            user.user_permissions.add(permiso1,permiso2)
            user.is_staff = True
            user.save()
            return HttpResponseRedirect(reverse('pasteleria:iniciar_sesion'))
    else:
        cliente.save()
        permiso1 = Permission.objects.get(name='Es comprador')
        permiso2 = Permission.objects.get(name='Can view producto')
        user = User.objects.create_user(run,email,password1)
        user.first_name = nombre
        user.last_name = paterno
        user.user_permissions.add(permiso1,permiso2)
        user.is_staff = True
        user.save()
        return HttpResponseRedirect(reverse('pasteleria:iniciar_sesion'))

#Iniciar Sesion
def iniciar_sesion (request):
    logout(request)
    return render(request,'pasteleria/iniciar_sesion.html')

#AUTENTICAR USUARIO
def autenticar_usuario (request):
    usuario = request.POST['rut']
    clave= request.POST['password']

    user = authenticate(request, username=usuario, password=clave)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('pasteleria:menu'))
    else:
        return render(request, 'pasteleria/iniciar_sesion.html', {
            'error_message': "Rut o Contraseña incorrectos"}) 
#CERRAR SESION
def cerrar_sesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('pasteleria:iniciar_sesion'))

#PRODUCTO
def producto(request,producto_id):
    if request.user.is_authenticated:
        p = Producto.objects.get(id=producto_id)
        context = {'producto':p,'sesion':'Cerrar sesión'}
        return render(request,'pasteleria/producto.html',context)
    else:
        p = Producto.objects.get(id=producto_id)
        context = {'producto':p,'mensaje_prod':'Debe iniciar sesión o registrarse para proceder con la compra.'}
        return render(request,'pasteleria/producto.html',context)  

#PAGO
def pago(request,producto_id):
    und = request.POST['und']
    stock = ''
    if request.user.username != 'admin_Cake':
        if und != "":
            p = Producto.objects.get(id=producto_id)
            cantidad = int(p.cantidad)-int(und)
            if cantidad < 0:
                stock += 'Stock disponible: ' + str(p.cantidad)
                context = {'producto':p,'mensaje':'No hay Stock disponible del producto,¡Intentenlo Nuevamente!.','sesion':'Cerrar sesión','stock': stock}
                return render(request,'pasteleria/producto.html',context)  
            else: 
                if request.user.has_perm('pasteleria.comprador') or request.user.has_perm('pasteleria.view_producto'):
                    context = {'producto':p,'cantidad':und}
                    return render(request,'pasteleria/pago.html',context)
                else:
                    p = Producto.objects.get(id=producto_id)
                    context = {'producto':p,'sesion':'Cerrar sesión', 'mensaje':'No posee los suficientes permisos para realizar esta accion.'}
                    return render(request,'pasteleria/pago_denegado.html',context)
                    
        else:
            return HttpResponseRedirect(reverse('pasteleria:producto'))
    else:
        p = Producto.objects.get(id=producto_id)
        context = {'producto':p,'sesion':'Cerrar sesión', 'mensaje':'No posee los suficientes permisos para realizar esta accion, ya que no posee un rut para generar la compra.'}
        return render(request,'pasteleria/pago_denegado.html',context)
#INSERTAR PAGO
def ingresar_pago(request,producto_id):
    p = Producto.objects.get(id=producto_id)
    run = request.user.username
    nombre = request.POST['nombre'].strip()
    ap_paterno = request.POST['paterno'].strip()
    ap_materno = request.POST['materno'].strip()
    direccion = request.POST['direccion'].strip()
    num_direc = request.POST['num'].strip()
    celular = request.POST['celular'].strip()
    email = request.POST['email'].strip()
    cardnumber = request.POST['cardnumber']
    expmonth =  request.POST['expmonth']
    expyear = request.POST['expyear']
    cvv = request.POST['cvv']
    cantidad = request.POST['cantidad']
    if cantidad != '':
        cli = Cliente.objects.get(run_cliente = run)
        pago = Pago(nombre_cliente = nombre, ap_paterno_cliente = ap_paterno, ap_materno_cliente = ap_materno, email_cliente = email, celular_cliente= celular,
        direccion_cliente = direccion, numeracion_clietne = num_direc, numero_tarjeta =  cardnumber, mes_expiracion = expmonth, anno_exiparacion = expyear, cvv = cvv )
        pago.producto = p
        pago.run_cliente = cli
        stock = int(p.cantidad) - int(cantidad)
        p.cantidad = stock 
        p.save() 
        pago.save()
        return HttpResponseRedirect(reverse('pasteleria:menu'))
    else:
        p = Producto.objects.get(id=producto_id)
        context = {'producto':p,'sesion':'Cerrar sesión'}
        return render(request,'pasteleria/producto.html',context)
#PAGO DENEGADO
def pago_denegado(request,producto_id):
    p = Producto.objects.get(id=producto_id)
    context = {'producto':p,'sesion':'Cerrar sesión', 'mensaje':'No posee los suficientes permisos para realizar esta accion.'}
    return render(request,'pasteleria/pago.html',context)

    