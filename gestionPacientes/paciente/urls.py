from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pacientes_view, name='pacientes_view'),
    path('<int:pk>/', views.paciente_view, name='ver_paciente_por_id'),
    path('analizar_eeg/<int:paciente_id>/', views.analizar_eeg_view)
    ]