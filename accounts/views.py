from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login, logout # for function based views
from django.contrib.auth import views as auth_view
from django.views.generic import View, TemplateView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class myLoginView(LoginView):
    authentication_form = LoginForm
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return self.request.GET.get('next') or reverse_lazy('accounts:home')

def register_view(request):
    if request.user.is_authenticated:
        redirect('accounts:home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfuly!")
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/home.html'

class MyLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('accounts:login')