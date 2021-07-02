from pasteleria.models import Ciudad, Cliente, Comuna, Producto
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['url', 'id', 'nombre_ciudad']

class ComunaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comuna
        fields = ['url', 'id', 'nombre_comuna']

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ['url', 'id', 'nombre_producto','descripcion','cantidad','precio']

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['url', 'id', 'run_cliente','nombre','ap_paterno','ap_materno','email','celular','direccion','numeracion','ciudad','comuna']