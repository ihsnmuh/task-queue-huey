from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModels


class Profile(BaseModels):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
