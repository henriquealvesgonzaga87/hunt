from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    email = models.EmailField(max_length=255, blank=False, unique=True, null=False)

    REQUIRED_FIELDS = ["email", "password"]

    class Config:
        db_table = "user"

    def __str__(self):
            return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
