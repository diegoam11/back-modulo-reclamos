from rest_framework import serializers
from .models import Queja

class QuejaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queja
        fields = '__all__'
        read_only_fields = ['id_queja']