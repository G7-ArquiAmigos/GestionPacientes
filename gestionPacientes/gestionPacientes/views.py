from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'gestionPacientes/index.html')

from django.shortcuts import redirect
from urllib.parse import urlencode
from django.conf import settings

def auth0_login(request):
    params = {
        'client_id': settings.SOCIAL_AUTH_AUTH0_KEY,
        'response_type': 'code',
        'redirect_uri': 'http://34.10.145.188:8000/gestionPacientes/home/',  # <-- debe coincidir con Auth0
        'scope': 'openid profile email',
        'state': 'secure_random_state_here'  # puedes usar una función para generarlo
    }
    return redirect(f'https://{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/authorize?{urlencode(params)}')

