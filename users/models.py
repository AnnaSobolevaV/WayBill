from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс для описания модели Пользователь
    User(email, first_name, last_name, phone, is_active)"""

    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    phone = models.CharField(
        max_length=35, verbose_name="Телефон", blank=True, null=True
    )
    is_active = models.BooleanField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
