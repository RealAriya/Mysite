from django.urls import path
from accounts.views import * 
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'accounts' 

urlpatterns = [
    # login
    path('login',views.login_view,name='login'),
    # logout
    path('logout',views.logout_view,name='logout'),
    # signup
    path('signup',views.signup_view,name='signup'),
    # Forget password
]
