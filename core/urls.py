from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reclamos/', include('api_reclamos.urls')),
    path('api/quejas/', include('api_quejas.urls')),
    path('api/solicitudes/', include('api_solicitudes.urls'))
]
