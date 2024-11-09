from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(models.Model, AbstractUser):
  username = models.CharField(max_length=50, unique=True, verbose_name="username", blank=False, null=False)
  email = models.EmailField(max_length=255, unique=True, verbose_name="e-mail", blank=False, null=False)
  password = models.CharField(max_length=50, verbose_name="password", blank=False, null=False)

  class Config:
    db_table = "user"

  def __str__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
