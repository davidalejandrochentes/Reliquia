from django.urls import path
from . import views

urlpatterns = [
    path('mantenimiento/', views.mantenimiento, name="mantenimiento_home"),
    path('area/', views.area, name="mantenimiento_area"),
    path('alertas/', views.area_alerta_mantenimiento, name='area_alerta_mantenimiento'),
    path('vista/', views.area_vista_mantenimiento, name="area_vista_mantenimiento"),
]