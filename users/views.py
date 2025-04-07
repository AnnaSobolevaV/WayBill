from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy


class LoginView(BaseLoginView):
    """Класс представлений для логина пользователя"""

    template_name = "users/login.html"
    success_url = reverse_lazy("mailing_list_mngr:home/")
