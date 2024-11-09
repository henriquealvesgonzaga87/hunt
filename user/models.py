from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  class Config:
    db_table = "user"

  def __str__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
