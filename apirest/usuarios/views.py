from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Usuario, Pedido, Perfil, Productos, Cliente, DatosPrivados
from .serializers import UsuarioSerializer, PedidoSerializer, PerfilSerializer, ProductosSerializer, ClienteSerializer, DatosPrivadosSerializer
from rest_framework.response import Response
import requests
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    

class PerfilListCreate(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer    
    
class ProductosListCreate(generics.ListCreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

class ProductosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer      

class ClienteListCreate(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Productos.objects.all()
    serializer_class = ClienteSerializer 

class ClimaAPIView(APIView):
    def get(self, request):
        url = "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener el clima"}, status=500)

class JorgeAPIView(APIView):
    def get(self, request):
        url = "http://18.221.57.79:8000/api"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de Jorge"}, status=500)
 
class CrisAPIView(APIView):
    def get(self, request):
        url = "http://3.19.235.79:8000/api"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de Cristian"}, status=500)

class RochaAPIView(APIView):
    def get(self, request):
        url = "http://18.190.176.232:8000/api/"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de Rocha"}, status=500)

class DatosPrivadosViewSet(viewsets.ModelViewSet):
    queryset = DatosPrivados.objects.all()
    serializer_class = DatosPrivadosSerializer


  
