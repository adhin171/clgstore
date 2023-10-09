from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.


def home(request):
    return render(request,'home.html')

def apply(request):
    return render(request,'apply.html')

def list_view(request):
    return render(request, 'list.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/apply/')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username1 = request.POST.get('username1')
        password1 = request.POST.get('password1')
        confirmpassword = request.POST.get('confirmpassword')

        if password1 == confirmpassword:
            user = User.objects.create_user(username=username1, password=password1)
            # Authenticate the user after registration
            auth_user = authenticate(request, username=username1, password=password1)
            if auth_user:
                login(request, auth_user)
                return redirect('/login_view/')  # Redirect to the home page or wherever you want
        else:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

    return render(request, 'register.html')


def submit_form(request):
    if request.method == 'POST':
        return redirect('/list/')
    return render(request, 'apply.html')

