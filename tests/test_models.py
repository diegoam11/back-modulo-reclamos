import pytest
from api_reclamos.models import Reclamo, TipoReclamo, Area
from django.utils import timezone

@pytest.mark.django_db
def test_reclamo_model_create():
    area = Area.objects.create(nombre="Área 1")
    tipo_reclamo = TipoReclamo.objects.create(nombre="Reclamo Tipo 1", id_area=area)
    reclamo = Reclamo.objects.create(
        id_cliente=1,
        id_tipo_reclamo=tipo_reclamo,
        tipo_bien_contratado=1,
        orden_compra=12345,
        codigo_producto=67890,
        fecha_compra=timezone.now().date(),
        forma_respuesta="Respuesta",
        fecha_reclamo=timezone.now().date(),
        detalle_reclamo="Detalles del reclamo",
        monto_reclamado="100.00",
        peticion_cliente="Petición del cliente",
        estado=1
    )
    
    assert reclamo.id_reclamo is not None
    assert reclamo.id_cliente == 1
    assert reclamo.monto_reclamado == "100.00"
    assert reclamo.estado == 1

@pytest.mark.django_db
def test_tipo_reclamo_model_create():
    area = Area.objects.create(nombre="Área 2")
    tipo_reclamo = TipoReclamo.objects.create(nombre="Reclamo Tipo 2", id_area=area)
    
    assert tipo_reclamo.id_tipo_reclamo is not None
    assert tipo_reclamo.nombre == "Reclamo Tipo 2"
    assert tipo_reclamo.id_area.nombre == "Área 2"

@pytest.mark.django_db
def test_area_model_create():
    area = Area.objects.create(nombre="Área 3")
    
    assert area.id_area is not None
    assert area.nombre == "Área 3"
