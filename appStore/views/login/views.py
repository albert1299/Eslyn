from django.contrib.auth.views import LoginView
from django.shortcuts import redirect


class LoginFormView(LoginView):
    template_name = 'login/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context
