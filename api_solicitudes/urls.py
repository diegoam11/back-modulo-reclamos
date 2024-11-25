from rest_framework import routers
from .views import SolicitudViewSet, TipoSolicitudViewSet
from django.urls import path

router = routers.DefaultRouter()

router.register('', SolicitudViewSet, 'solicitudes')

urlpatterns = [
    path('tipo/', TipoSolicitudViewSet.as_view({'get': 'list'})),
    path('<int:id_solicitud>/', SolicitudViewSet.as_view({'get': 'retrieve'})),
    path('cliente/<int:id_cliente>/', SolicitudViewSet.as_view({'get': 'get_by_client'}))
] + router.urls