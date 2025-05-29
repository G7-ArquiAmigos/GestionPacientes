"""gestionPacientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# gestionPacientes/urls.py
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from . import views

urlpatterns = [
    path('gestionPacientes/admin/', admin.site.urls),
    path('gestionPacientes/home/', views.index, name='home'),
    path('gestionPacientes/', include('paciente.urls')),
    path('gestionPacientes/', include('django.contrib.auth.urls')),
    path('gestionPacientes/', include('social_django.urls')), # <--- ¡ASEGÚRATE DE QUE ESTÉ ASÍ!
    path('gestionPacientes/login/auth0/', views.auth0_login, name='auth0_login'),
    path('gestionPacientes/auth/complete/auth0?/', lambda request: redirect('/gestionPacientes/complete/auth0?/' + request.META['QUERY_STRING'])),
]
