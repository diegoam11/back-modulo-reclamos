from rest_framework import routers
from .views import ReclamoViewSet, TipoReclamoViewSet
from django.urls import path

router = routers.DefaultRouter()

router.register('', ReclamoViewSet, 'reclamos')

urlpatterns =  [
    path('tipo/', TipoReclamoViewSet.as_view({'get': 'list'})),
    path('<int:id_reclamo>/', ReclamoViewSet.as_view({'get': 'retrieve'})),
    path('cliente/<int:id_cliente>/', ReclamoViewSet.as_view({'get': 'get_by_client'})),
] + router.urls 
