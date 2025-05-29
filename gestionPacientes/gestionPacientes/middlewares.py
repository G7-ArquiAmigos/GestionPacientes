# middlewares.py
import base64, json
from django.contrib.auth.models import AnonymousUser
from django.utils.functional import SimpleLazyObject

def get_user_from_request(request):
    encoded = request.headers.get("X-Userinfo")
    if not encoded:
        return AnonymousUser()

    try:
        decoded_json = base64.b64decode(encoded).decode("utf-8")
        userinfo = json.loads(decoded_json)

        class Auth0User:
            def __init__(self, info):
                self.email = info.get("email")
                self.name = info.get("name")
                self.roles = info.get("https://dev-znond25bgndcf8ju.us.auth0.com/roles", [])
                self.is_authenticated = True

            def has_role(self, role):
                return role in self.roles

        return Auth0User(userinfo)

    except Exception:
        return AnonymousUser()

class Auth0UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: get_user_from_request(request))
        return self.get_response(request)
