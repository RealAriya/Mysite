from django.shortcuts import render,get_object_or_404
from django.http import Http404
from blog.models import post
from django.utils import timezone




def blog_home(request):
    now = timezone.now()
    posts = post.objects.filter(status = 1 , published_date__lte=now)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    posts = get_object_or_404(post, id=pid)

    posts + 1
    
    context = {'posts': posts}
    return render(request,'blog/blog-single.html',context)







########################################################### test

# def test(request,pid):
#     # posts = post.objects.all()
#     posts = post.objects.filter(pk=pid)
#     # posts = post.objects.get(id=pid)
#     # posts = get_object_or_404(post,pk=pid)  #posts = get_object_or_404(name of class , name=pid)
#     if not posts.exists():
#         raise Http404("Post not found")
#     context = {'posts': posts}
#     return render(request,'test.html',context)

