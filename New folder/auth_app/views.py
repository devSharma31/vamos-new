from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import RegistrationForm

        
def index(request):
    return render(request, 'ecom_app/index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully.', extra_tags='success')  # Add success message
            return redirect('Home')  # Redirect to the homepage
        else:
            messages.warning(request, 'Invalid credentials. Please try again.', extra_tags='error')# Add error message

        if not user.profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect('uth_app/registration/login.html')

    # Handle the case for GET request or failed login
    return render(request, 'auth_app/registration/login.html')

@login_required  # This decorator ensures that the user is logged in to access this view.
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.', extra_tags='success')
    return redirect('Home')

def password_reset(request):
    # Implement your password reset logic here
    return render(request, 'auth_app/password_reset.html')



def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(username = email)

        if user.exists():
            messages.warning(request, 'Email is already exists.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user.set_password(password)
        user.save()

        messages.success(request, 'An email has been sent for verification.')
        return HttpResponseRedirect('login')


    return render(request ,'auth_app/registration/register.html')

def email_verification(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
