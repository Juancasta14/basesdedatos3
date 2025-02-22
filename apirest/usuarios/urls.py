from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .routers import UsuarioViewSet, PedidoViewSet
from .views import ClimaAPIView, JorgeAPIView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pedidos', PedidoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('clima/', ClimaAPIView.as_view(), name='clima-api'), 
    path('jorge/', JorgeAPIView.as_view(), name='Jorge-api'), 
   
]

