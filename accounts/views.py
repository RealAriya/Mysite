from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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

# def logout_view(request):
#     pass

def signup_view(request):
    return render(request,'accounts/signup.html') 