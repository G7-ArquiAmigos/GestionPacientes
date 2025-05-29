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

def auth0_login(request):
    # Construye la URL de redirección correcta usando reverse o codificándola si es necesario,
    # pero DEBE apuntar al endpoint de callback de Auth0 de social_django.
    # El espacio de nombres 'social' es usualmente agregado por social_django.urls
    # y 'complete' es la vista que maneja el callback.
    # 'auth0' es el nombre del backend.

    try:
        # Esto asume que tus social_django.urls están configuradas con el namespace 'social'
        # y que la URL completa tiene el nombre del backend 'auth0'.
        # Patrón común: namespace:complete_backend_name
        redirect_uri_path = reverse('social:complete', args=('auth0',))
    except Exception:
        # Fallback si reverse no funciona (ej. si social_django.urls no tiene el namespace 'social')
        # Este es el patrón más común para social_django + Auth0 cuando se prefija con 'gestionPacientes/'
        redirect_uri_path = '/gestionPacientes/auth/complete/auth0/'

    # Asegúrate de que se usa la URL absoluta completa para redirect_uri
    redirect_uri = request.build_absolute_uri(redirect_uri_path)

    params = {
        'client_id': settings.SOCIAL_AUTH_AUTH0_KEY,
        'response_type': 'code',
        'redirect_uri': redirect_uri,  # <--- ¡ESTA ES LA SOLUCIÓN!
        'scope': 'openid profile email',
        'state': 'secure_random_state_here' # Para mayor seguridad, genera esto dinámicamente y guárdalo en la sesión
    }
    return redirect(f'https://{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/authorize?{urlencode(params)}')
