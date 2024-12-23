from django.contrib import admin

from user.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
  list_display = ("user",)
