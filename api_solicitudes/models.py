from django.db import models
from api_reclamos.models import Area  

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    id_tipo_solicitud = models.ForeignKey(
        'TipoSolicitud',
        on_delete=models.CASCADE,
        related_name='solicitudes'
    )

    tipo_bien_contratado = models.IntegerField()
    orden_compra = models.IntegerField()
    codigo_producto = models.IntegerField()

    forma_respuesta = models.CharField(max_length=255)
    fecha_solicitud = models.DateField()

    detalle_solicitud = models.TextField()
    peticion_cliente = models.TextField()

    acciones_tomadas = models.TextField(blank=True, null=True)
    estado = models.IntegerField()
    fecha_respuesta = models.DateField(blank=True, null=True)
    fecha_limite = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'solicitud'
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'
        ordering = ['fecha_solicitud']

    def __str__(self):
        return f'Solicitud {self.id_solicitud} - Cliente {self.id_cliente}'


from django.db import models

class TipoSolicitud(models.Model):
    id_tipo_solicitud = models.AutoField(primary_key=True)
    id_area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        related_name='tipos_solicitud'
    )
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'tipo_solicitud'