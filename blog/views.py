from django.shortcuts import render,get_object_or_404
from django.http import Http404
from blog.models import post



def blog_home(request):
    posts = post.objects.filter(status = 1)
    context = {'post_1':'Bitcoin crashed', 'post_2':'Gold rise up', 'post_3':'Barca win all games','post_4':'Real Madrid vs Dortmond',
               'posts': posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')

def test(request,pid):
    # posts = post.objects.all()
    posts = post.objects.filter(pk=pid)
    # posts = post.objects.get(id=pid)
    # posts = get_object_or_404(post,pk=pid)  #posts = get_object_or_404(name of class , name=pid)
    if not posts.exists():
        raise Http404("Post not found")
    context = {'posts': posts}
    return render(request,'test.html',context)

