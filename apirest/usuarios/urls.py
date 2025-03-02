from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import UsuarioViewSet, PedidoViewSet , PerfilViewSet, ProductosViewSet, ClienteViewSet
from .views import ClimaAPIView, JorgeAPIView, DatosPrivadosViewSet, DatosPrivadosCorreoViewSet, EnvioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'perfil_mibd_jorge', PerfilViewSet)
router.register(r'productos_mibd_cristian', ProductosViewSet)
router.register(r'clientes_mibd_rocha', ClienteViewSet)
router.register(r'datos_privados', DatosPrivadosViewSet)
router.register(r'datos_privados_correo', DatosPrivadosCorreoViewSet)
router.register(r'datos_publicos_envios', EnvioViewSet)
urlpatterns = [
    path('', include(router.urls)),
    
   
]

