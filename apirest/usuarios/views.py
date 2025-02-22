from rest_framework import generics
from .models import Usuario, Pedido
from .serializers import UsuarioSerializer, PedidoSerializer

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
        url = "http://18.221.57.79:8000/api/Perfil"
        response = requests.get(url)

        if response.status_code == 200:
            return Response(response.json())  
        else:
            return Response({"error": "No se pudo obtener la API de Jorge"}, status=500)           
