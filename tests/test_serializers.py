import pytest
from api_reclamos.models import Reclamo, TipoReclamo, Area
from api_reclamos.serializers import ReclamoSerializer, TipoReclamoSerializer, AreaSerializer
from rest_framework.exceptions import ValidationError

@pytest.mark.django_db
def test_reclamo_serializer():
    area = Area.objects.create(nombre="Área de prueba")
    tipo_reclamo = TipoReclamo.objects.create(nombre="Reclamo Tipo de prueba", id_area=area)
    reclamo = Reclamo.objects.create(
        id_cliente=1,
        id_tipo_reclamo=tipo_reclamo,
        tipo_bien_contratado=1,
        orden_compra=12345,
        codigo_producto=67890,
        fecha_compra="2024-11-01",
        forma_respuesta="Respuesta",
        fecha_reclamo="2024-11-01",
        detalle_reclamo="Detalles",
        monto_reclamado="100.00",
        peticion_cliente="Petición",
        estado=1
    )
    
    serializer = ReclamoSerializer(reclamo)
    assert serializer.data['id_cliente'] == 1
    assert serializer.data['monto_reclamado'] == "100.00"

@pytest.mark.django_db
def test_tipo_reclamo_serializer():
    area = Area.objects.create(nombre="Área de prueba")
    tipo_reclamo = TipoReclamo.objects.create(nombre="Reclamo Tipo de prueba", id_area=area)
    
    serializer = TipoReclamoSerializer(tipo_reclamo)
    assert serializer.data['nombre'] == "Reclamo Tipo de prueba"
    assert 'id_area' in serializer.data

@pytest.mark.django_db
def test_area_serializer():
    area = Area.objects.create(nombre="Área de prueba")
    
    serializer = AreaSerializer(area)
    assert serializer.data['nombre'] == "Área de prueba"
