from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    address = models.CharField(max_length=100)
