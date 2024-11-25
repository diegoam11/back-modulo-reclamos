from .models import Solicitud, TipoSolicitud
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import SolicitudSerializer, TipoSolicitudSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SolicitudSerializer
    lookup_field = 'id_solicitud'
    
    def get_by_client(self, request, id_cliente=None):
        solicitudes = Solicitud.objects.filter(id_cliente=id_cliente)
        serializer = SolicitudSerializer(solicitudes, many=True)
        return Response(serializer.data)
    
class TipoSolicitudViewSet(viewsets.ModelViewSet):
    queryset = TipoSolicitud.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoSolicitudSerializer

