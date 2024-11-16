from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "Your logged in successfully.")
            return redirect('/')
        
    
    return render(request,'accounts/login.html')

# def logout_view(request):
#     pass

def signup_view(request):
    return render(request,'accounts/signup.html') 