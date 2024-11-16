from django.shortcuts import render

def login_view(request):
    if request.user.is_authenticated:
        message = f' User is authenticated as {request.user.username}'
    else:
        message = f' User is not authenticated as {request.user.username}'
    
    context={
        'message':message
    }
    return render(request,'accounts/login.html',context)

# def logout_view(request):
#     pass

def signup_view(request):
    return render(request,'accounts/signup.html') 