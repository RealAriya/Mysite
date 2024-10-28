from django.shortcuts import render
from blog.models import post



def blog_home(request):
    context = {'post_1':'Bitcoin crashed', 'post_2':'Gold rise up', 'post_3':'Barca win all games','post_4':'Real Madrid vs Dortmond'}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test(request):
    posts = post.objects.all()
    context = {'posts': posts}
    return render(request,'test.html',context)

