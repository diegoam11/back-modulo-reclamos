from rest_framework import serializers
from .models import Reclamo, TipoReclamo, Area

class ReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reclamo
        fields = '__all__'
        read_only_fields = ['id_reclamo']
        
class TipoReclamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoReclamo
        fields = '__all__'
        read_only_fields = ['id_tipo_reclamo']
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
        read_only_fields = ['id_area']