from django.urls import path
from . import views

urlpatterns = [
    path('mantenimiento/', views.mantenimiento, name="mantenimiento_home")
]