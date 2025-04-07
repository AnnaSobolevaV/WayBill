from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    """Класс формы создания Пользователя"""

    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """Класс формы изменения Пользователя"""

    class Meta:
        model = User
        fields = ("email",)
