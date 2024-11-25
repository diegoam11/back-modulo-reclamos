# Generated by Django 5.1.3 on 2024-11-24 21:08

import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
                'db_table': 'area',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoReclamo',
            fields=[
                ('id_tipo_reclamo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipos_reclamo', to='api_reclamos.area')),
            ],
            options={
                'verbose_name': 'Tipo de Reclamo',
                'verbose_name_plural': 'Tipos de Reclamo',
                'db_table': 'tipo_reclamo',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id_reclamo', models.AutoField(primary_key=True, serialize=False)),
                ('id_cliente', models.IntegerField()),
                ('tipo_bien_contratado', models.IntegerField()),
                ('orden_compra', models.IntegerField()),
                ('codigo_producto', models.IntegerField()),
                ('fecha_compra', models.DateField()),
                ('forma_respuesta', models.CharField(max_length=255)),
                ('fecha_reclamo', models.DateField()),
                ('detalle_reclamo', models.TextField()),
                ('monto_reclamado', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('peticion_cliente', models.TextField()),
                ('acciones_tomadas', models.TextField(blank=True, null=True)),
                ('estado', models.IntegerField()),
                ('fecha_respuesta', models.DateField(blank=True, null=True)),
                ('fecha_limite', models.DateField(blank=True, null=True)),
                ('id_tipo_reclamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reclamos', to='api_reclamos.tiporeclamo')),
            ],
        ),
    ]