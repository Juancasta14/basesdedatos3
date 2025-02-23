from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import UsuarioViewSet, PedidoViewSet , PerfilViewSet, ProductosViewSet, ClienteViewSet
from .views import ClimaAPIView, JorgeAPIView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'perfil_mibd_jorge', PerfilViewSet)
router.register(r'productos_mibd_cristian', ProductosViewSet)
router.register(r'clientes_mibd_rocha', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
   
]

