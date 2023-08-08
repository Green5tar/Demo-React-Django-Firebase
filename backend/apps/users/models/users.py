from django.db import models
from users.models.mixins import TimeStampedModel


class User(TimeStampedModel):
    """Base user model"""

    email = models.EmailField(unique=True)
    firebase_id = models.TextField(unique=True)
