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
    postss = post.objects.filter(status = 1)
    posts = get_object_or_404(postss, id=pid)

    all_posts = list(postss)

    current_index = all_posts.index(posts)

    pre_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None

    posts + 1
    
    context = {
        'posts': posts,
        'pre_post': pre_post,
        'next_post': next_post
               }
    
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

