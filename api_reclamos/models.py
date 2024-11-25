from django.db import models
from decimal import Decimal
#from strategies.strategies import ResponseStrategy

class Reclamo(models.Model):
    id_reclamo = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    id_tipo_reclamo = models.ForeignKey('TipoReclamo', on_delete=models.CASCADE, related_name='reclamos')

    tipo_bien_contratado = models.IntegerField()
    orden_compra = models.IntegerField()
    codigo_producto = models.IntegerField()
    fecha_compra = models.DateField()

    forma_respuesta = models.CharField(max_length=255)
    fecha_reclamo = models.DateField()

    detalle_reclamo = models.TextField()
    monto_reclamado = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    peticion_cliente = models.TextField()

    acciones_tomadas = models.TextField(blank=True, null=True)
    estado = models.IntegerField()
    fecha_respuesta = models.DateField(blank=True, null=True)
    fecha_limite = models.DateField(blank=True, null=True)

    # Campo personalizado para la estrategia de respuesta
    #response_strategy: ResponseStrategy = None
    
    class Meta:
        db_table = 'reclamo'  

class TipoReclamo(models.Model):
    id_tipo_reclamo = models.AutoField(primary_key=True)
    id_area = models.ForeignKey('Area', on_delete=models.CASCADE, related_name='tipos_reclamo') 
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_reclamo'  

class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'area'  

