from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        req_username = request.POST.get('username')
        req_password = request.POST.get('password')

        if req_username and req_password:
            user = auth.authenticate(username=req_username, password=req_password)
            if user:
                auth.login(request, user)
                return redirect('hospitals')
            return redirect('login')
        return redirect('login')

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        req_username = request.POST.get('username')
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')

        user = User.objects.create_user(email=req_email, username=req_username)
        user.set_password(req_password)
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.save()
        return render(request, 'authentication/register.html')
