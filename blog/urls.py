from django.urls import path
from blog.views import *   
from blog.feeds import LatestEntriesFeed

app_name = 'blog' 

urlpatterns = [
    path('', blog_home, name='home'),
    path('<int:pid>', blog_single, name='single'),
    path('test',test,name = 'test'),
    path('category/<str:cat_name>', blog_home, name='category'),
    path('tag/<str:tag_name>', blog_home, name='tag'),
    path('author/<str:author_username>/',blog_home,name='author'),
    path('search/',blog_search,name='search'),
    path("rss/feed/", LatestEntriesFeed()),
]

