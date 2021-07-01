import datetime
from django.db import models
from django.utils import timezone

class Comuna(models.Model):
    nombre_comuna = models.CharField(max_length=200)
    fecha_comuna = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre_comuna

    def was_published_recently(self):
        return self.pub_fecha >= timezone.now() - datetime.timedelta(days=1)

class Ciudad(models.Model):
    nombre_ciudad = models.CharField(max_length=200)
    fecha_ciudad = models.DateTimeField('date published')
    def __str__(self):
        return self.nombre_ciudad

    def was_published_recently(self):
        return self.pub_fecha >= timezone.now() - datetime.timedelta(days=1)


class Cliente(models.Model):
    run_cliente = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    ap_paterno = models.CharField(max_length=200)
    ap_materno = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    celular = models.CharField(max_length=12)
    direccion = models.CharField(max_length=200)
    numeracion = models.IntegerField(default=0)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    password = models.CharField(max_length=12)
    fecha_cliente = models.DateTimeField('date published')
   
    def __str__(self):
        return self.run_cliente

    def was_published_recently(self):
        return self.pub_fecha >= timezone.now() - datetime.timedelta(days=1)


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre_producto

class Pago(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    run_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=200)
    ap_paterno_cliente = models.CharField(max_length=200)
    ap_materno_cliente = models.CharField(max_length=200)
    email_cliente = models.CharField(max_length=200)
    celular_cliente = models.CharField(max_length=12)
    direccion_cliente = models.CharField(max_length=200)
    numeracion_clietne = models.IntegerField(default=0)
    numero_tarjeta = models.IntegerField(default=0)
    mes_expiracion = models.IntegerField(default=0)
    anno_exiparacion = models.IntegerField(default=0)
    cvv = models.IntegerField(default=0)
    

    def __str__(self):
        return'{} - {}'.format(self.run_cliente,self.producto)