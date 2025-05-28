from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.pacientes_view, name='pacientes_view'),
    path('<int:pk>/', views.paciente_view, name='paciente_view'),
    path('analizar_eeg/<int:paciente_id>/', views.analizar_eeg_view)
    ]