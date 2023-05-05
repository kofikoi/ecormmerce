from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.views import View
from django.urls import reverse, reverse_lazy

class LoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('product_list')  # change this to the URL you want to redirect to

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return '/admin/'
            else:
                  return '/vehicle_list/'
        else:
              return '/login/'


class HomeView(View):
    def get(self, request):
        login_url = reverse('login')
        return render(request, 'home.html', {'login_url': login_url})


def logout_view(request):
    logout(request)
    return redirect('home')