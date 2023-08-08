from apps.users.models import User
from rest_framework.authentication import BaseAuthentication
from portfolio.firebase_conf.exceptions import (
    FirebaseError,
    InvalidAuthToken,
    NoAuthToken,
)
from firebase_admin import auth


class FirebaseAuthenticationBackend(BaseAuthentication):
    def authenticate(self, request, token=None):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        print("Authentication token", auth_header)
        if not auth_header:
            raise NoAuthToken("No auth token provided")
        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
        if not id_token or not decoded_token:
            return None
        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()
        user, _ = User.objects.get_or_create(username=uid)
        return (user, None)
