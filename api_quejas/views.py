from .models import Queja
from rest_framework import viewsets, permissions
from .serializers import QuejaSerializer
from rest_framework.response import Response

class QuejaViewSet(viewsets.ModelViewSet):
    queryset = Queja.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuejaSerializer
    lookup_field = 'id_queja'
    
    def get_by_client(self, request, id_cliente=None):
        quejas = Queja.objects.filter(id_cliente=id_cliente)
        serializer = QuejaSerializer(quejas, many=True)
        return Response(serializer.data)

