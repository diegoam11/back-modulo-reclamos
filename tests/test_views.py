import pytest
from rest_framework.test import APIClient
from api_reclamos.models import Reclamo, TipoReclamo, Area
from django.urls import reverse

@pytest.mark.django_db
def test_reclamo_viewset():
    client = APIClient()
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
    
    url = reverse('reclamo-list')  
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) > 0

@pytest.mark.django_db
def test_reclamo_by_client_view():
    client = APIClient()
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
    
    url = reverse('reclamo-by-client', kwargs={'id_cliente': 1})  
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
