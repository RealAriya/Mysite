from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = request.POST["username"]
                password = request.POST["password"]
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "Your logged in successfully.")
                    return redirect('/')
            
        form = AuthenticationForm() 
        context = {
            'form': form
        }   
    
        return render(request,'accounts/login.html',context)
    else:
        messages.add_message(request, messages.INFO, "You already logged in..")
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