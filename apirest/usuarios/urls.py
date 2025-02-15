from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import UsuarioViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

