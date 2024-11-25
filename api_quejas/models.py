from django.db import models

class Queja(models.Model):
    id_queja = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()

    tipo_bien_contratado = models.IntegerField()
    orden_compra = models.IntegerField()
    codigo_producto = models.IntegerField()
    fecha_compra = models.DateField()

    forma_respuesta = models.CharField(max_length=255)
    fecha_queja = models.DateField()

    detalle_queja = models.TextField()
    peticion_cliente = models.TextField()

    acciones_tomadas = models.TextField(blank=True, null=True)
    estado = models.IntegerField()
    fecha_respuesta = models.DateField(blank=True, null=True)
    fecha_limite = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'queja' 
