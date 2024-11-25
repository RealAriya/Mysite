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

    path('reset-password/',
          auth_views.PasswordResetView.as_view(
          template_name="registration/password_reset_email.html"), 
          name='password_reset'),
    path('reset-password-sent/',
          auth_views.PasswordResetDoneView.as_view(
          template_name="registration/password-sent.html"),
          name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(
          template_name="registration/password_change_form.html"), 
          name='password_reset_confirm'),
    path('reset-password-complete/',
          auth_views.PasswordResetCompleteView.as_view(
          template_name="registration/password_reset_complete.html"), 
          name='password_reset_complete'),
]
