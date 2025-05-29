from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'gestionPacientes/index.html')

from django.shortcuts import redirect
from urllib.parse import urlencode
from django.conf import settings

from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
from django.urls import reverse # Agrega esta importación para usar reverse

from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlencode
# from django.urls import reverse # Ya no la usaremos para construir el redirect_uri directamente

def auth0_login(request):
    # La URL pública a la que Auth0 debe redirigir.
    # Asume que tu Kong está en 'tu-dominio-publico.com' (o la IP pública de Kong)
    # y que el path que Kong redirige a /gestionPacientes/complete/auth0 es /gestionPacientes/complete/auth0
    # CAMBIA 'http://tu-dominio-publico.com' por la IP pública de tu Kong o su dominio.
    # Y asegúrate que el puerto 8080 sea accesible públicamente a través de Kong, si ese es el puerto que Auth0 debe usar
    # o el puerto estándar 80/443 si Kong hace la traducción de puertos.

    # Si Kong está accesible en http://<IP_PUBLICA_KONG>:<PUERTO_KONG>/gestionPacientes/auth/complete/auth0/
    PUBLIC_KONG_URL_BASE = 'http://34.10.145.188:8000' # <--- ¡CAMBIA ESTO! Por tu IP/Dominio público de Kong y puerto.

    redirect_uri_path = '/gestionPacientes/auth/complete/auth0/' # Este es el path que social-auth-app-django espera

    redirect_uri = f"{PUBLIC_KONG_URL_BASE}{redirect_uri_path}"


    params = {
        'client_id': settings.SOCIAL_AUTH_AUTH0_KEY,
        'response_type': 'code',
        'redirect_uri': redirect_uri,  # <--- ¡AQUÍ ESTÁ EL CAMBIO CRÍTICO!
        'scope': 'openid profile email',
        'state': 'secure_random_state_here' # Para seguridad, genera esto dinámicamente
    }
    return redirect(f'https://{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/authorize?{urlencode(params)}')