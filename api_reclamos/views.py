from .models import Reclamo, TipoReclamo, Area
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import ReclamoSerializer, TipoReclamoSerializer, AreaSerializer

class ReclamoViewSet(viewsets.ModelViewSet):
    queryset = Reclamo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReclamoSerializer
    lookup_field = 'id_reclamo'
    
    def get_by_client(self, request, id_cliente=None):
        reclamos = Reclamo.objects.filter(id_cliente=id_cliente)
        serializer = ReclamoSerializer(reclamos, many=True)
        return Response(serializer.data)
    
class TipoReclamoViewSet(viewsets.ModelViewSet):
    queryset = TipoReclamo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoReclamoSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AreaSerializer

