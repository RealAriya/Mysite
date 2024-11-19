from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = None
            
            # Authenticate with username if provided
            if username:
                user = authenticate(request, username=username, password=password)
                
            # Authenticate with email if user is still None and email is provided
            if user is None and email:
                users = User.objects.filter(email=email)
                if users.exists():
                    user = authenticate(request, username=users.first().username, password=password)

            # If user is authenticated
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "You are logged in successfully.")
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Invalid credentials.")
        else:
            # Display an empty form if it's a GET request
            form = AuthenticationForm()
        
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        messages.add_message(request, messages.INFO, "You are already logged in.")
        return redirect('/')

@login_required             # we use this instead of : if not request.user.is_authenticated:
def logout_view(request):
    
    logout(request)
    return redirect('/')



def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                    form.save()
                    messages.add_message(request, messages.SUCCESS, "You signed up successfully.")
                    return redirect('/')
            
        form = UserCreationForm()

        context = {
            'form':form
        }
        return render(request,'accounts/signup.html',context) 
    else:
        return redirect('/')


def forget_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            email = request.POST.get("email")
            