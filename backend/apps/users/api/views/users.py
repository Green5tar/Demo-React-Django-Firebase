from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.api.serializers import SignUpSerializer
from users.models import User

from portfolio.firebase_conf.authentication import FirebaseAuthenticationBackend


class UsersAPIView(ListCreateAPIView):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    lookup_field = "firebase_id"

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_authenticators(self):
        if self.request.method == "POST":
            return []
        return [FirebaseAuthenticationBackend()]
