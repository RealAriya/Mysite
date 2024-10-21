from django.urls import path
from blog.views import *   

app_name = 'blog' 

urlpatterns = [
    path('blog', blog_home, name="home"),
    path('blog/single', blog_single, name="single"),
    
]

