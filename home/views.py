from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'index.html'


class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    success_url = '/orders'


class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = '/login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/orders')
        return super().get(request, *args, **kwargs)
