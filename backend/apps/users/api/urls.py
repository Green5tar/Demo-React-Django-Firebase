from django.urls import path
from users.api.views import UsersAPIView

urlpatterns = [
    path("", UsersAPIView.as_view()),
]
