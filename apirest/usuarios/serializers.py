from rest_framework import serializers
from .models import Usuario, Pedido, Perfil, Productos, Cliente, DatosPrivados, Trip, Envio

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    pedidos = PedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = '__all__'


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
class DatosPrivadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPrivados
        fields = ['product_name']
        
        
class DatosPrivadosCorreoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        
class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envio
        fields = '__all__'
