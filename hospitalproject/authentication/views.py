from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.mail import send_mail

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

class LogoutView(View):
    def post(self, request):
        auth.logout
        messages.success(request, "You're logged out")
        return redirect("login")

class RegisterView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        req_username = request.POST.get('username')
        req_email = request.POST.get('email')
        req_password = request.POST.get('password')

        user = User.objects.filter(username=req_username).exists()
        if not user:
            user = User.objects.filter(email=req_email).exists()
            if not user:
                user = User.objects.create_user(email=req_email, username=req_username)
                user.set_password(req_password)
                user.is_active = True
                user.is_staff = False
                user.is_superuser = False
                user.save()

                send_mail(
                    'Account Creation', # subject
                    'Congratulations! Your account has been created.', # message
                    'c4crypt@gmail.com', # sender
                    [user.email] # receiver
                )

                return render(request, 'authentication/register.html')
            messages.error(request, 'Email already taken, try another!!')
            return render(request, 'authentication/register.html')
        messages.error(request, 'Username already taken, try another!!')
        return render(request, 'authentication/register.html') 
