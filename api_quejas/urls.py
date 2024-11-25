from rest_framework import routers
from .views import QuejaViewSet
from django.urls import path

router = routers.DefaultRouter()

router.register('', QuejaViewSet, 'quejas')

urlpatterns = [
    path('<int:id_queja>/', QuejaViewSet.as_view({'get': 'retrieve'})),
    path('cliente/<int:id_cliente>/', QuejaViewSet.as_view({'get': 'get_by_client'}))
] + router.urls