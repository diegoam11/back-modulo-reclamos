from rest_framework import serializers
from .models import Solicitud, TipoSolicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
        read_only_fields = ['id_solicitud']
        
class TipoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSolicitud
        fields = '__all__'
        read_only_fields = ['id_tipo_solicitud']