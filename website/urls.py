from django.urls import path
from website.views import *   


urlpatterns = [
    path('', index_view),
    path('about', about_view),
    path('contact', contact_view),
    path('forms',first_site),
    path('mp4', mp4_site)
]
