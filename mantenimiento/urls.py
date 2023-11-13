from django.urls import path
from . import views

urlpatterns = [
    path('mantenimiento/', views.mantenimiento, name="mantenimiento_home"),
    path('area/', views.area, name="mantenimiento_area"),
    path('alertas/', views.alerta_mantenimiento, name='mantenimiento_alertas'),
    path('vista/', views.vista, name="mantenimiento_vista"),
]