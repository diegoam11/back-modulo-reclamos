from django.contrib import admin
from .models import Solicitud, TipoSolicitud

admin.site.register(Solicitud)
admin.site.register(TipoSolicitud)