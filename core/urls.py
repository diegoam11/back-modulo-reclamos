from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Reclamos, Quejas y Solicitudes",
      default_version='v1',
      description="Test description",
      license=openapi.License(name="BSD License"),
   ),
   public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/reclamos/', include('api_reclamos.urls')),
    path('api/quejas/', include('api_quejas.urls')),
    path('api/solicitudes/', include('api_solicitudes.urls')),
    #docs
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
