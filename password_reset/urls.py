from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'password_reset'

urlpatterns = [
    path('reset-password/',
          auth_views.PasswordResetView.as_view(
          template_name="password_reset/password_reset_email.html"), 
          name='password_reset'),
    path('reset-password-sent/',
          auth_views.PasswordResetDoneView.as_view(
          template_name="password_reset/password_reset_sent.html"),
          name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(
          template_name="password_reset/password_reset_confirm.html"), 
          name='password_reset_confirm'),
    path('reset-password-complete/',
          auth_views.PasswordResetCompleteView.as_view(
          template_name="password_reset/password_reset_complete.html"), 
          name='password_reset_complete'),
]
