from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == 'POST':
#             username = request.POST.get("username")
#             email = request.POST.get("email")
#             password = request.POST.get("password")
#             user = None
        
#             if username:
#                 user = authenticate(request, username=username, password=password)
                
#             if user is None and email:
#                 users = User.objects.filter(email=email)
#                 if users.exists():
#                     user = authenticate(request, username=users.first().username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.add_message(request, messages.SUCCESS, "You are logged in successfully.")
#                 return redirect('/')
#             else:
#                 messages.add_message(request, messages.ERROR, "Invalid credentials.")
#         else:
            
#             form = AuthenticationForm()
        
#         context = {'form': form}
#         return render(request, 'accounts/login.html', context)
#     else:
#         messages.add_message(request, messages.INFO, "You are already logged in.")
#         return redirect('/')



def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_or_email = request.POST.get('username_or_email')
            password = request.POST.get('password')
            user = None
            
            # Check if the input is an email or username
            if '@' in username_or_email:
                # If it's an email
                try:
                    user = authenticate(request, username=User.objects.get(email=username_or_email).username, password=password)
                except User.DoesNotExist:
                    user = None
            else:
                # If it's a username
                user = authenticate(request, username=username_or_email, password=password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "You logged in successfully.")
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, "Invalid credentials.")
        
        # Render the login form (optional to show the form again)
        form = AuthenticationForm()  # Still good to keep this for rendering
        context = {
            'form': form
        }
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
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            # Validate data
            if not username or not email or not password1 or not password2:
                messages.error(request, "All fields are required.")
            elif password1 != password2:
                messages.error(request, "Passwords do not match.")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already in use.")
            else:
                # Create user
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, "You signed up successfully.")
                return redirect('/')

        return render(request, 'accounts/signup.html')

    return redirect('/')


