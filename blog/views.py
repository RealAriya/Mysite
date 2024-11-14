from django.shortcuts import render,get_object_or_404
from django.http import Http404
from blog.models import post,Comment
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage



def blog_home(request,**kwargs):
    now = timezone.now()
    posts = post.objects.filter(status = 1 , published_date__lte=now)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get("page")
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
         posts = posts.get_page(1)

    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)


def blog_single(request,pid):
    now = timezone.now()
    postss = post.objects.filter(status = 1 , published_date__lte=now)
    posts = get_object_or_404(postss, id=pid)
    comments = Comment.objects.filter(post=posts.id,approved=1).order_by('created_date')
    all_posts = list(postss)

    current_index = all_posts.index(posts)

    pre_post = all_posts[current_index - 1] if current_index > 0 else None
    next_post = all_posts[current_index + 1] if current_index < len(all_posts) - 1 else None

    posts + 1
    
    context = {
        'posts': posts,
        'pre_post': pre_post,
        'next_post': next_post,
        'comments': comments,
               }
    
    return render(request,'blog/blog-single.html',context)


def blog_search(request):
    now = timezone.now()
    posts = post.objects.filter(status = 1 , published_date__lte=now)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request,'blog/blog-home.html',context)



# def blog_category(request,cat_name):
#     now = timezone.now()
#     posts = post.objects.filter(status = 1, published_date__lte=now)
#     posts = posts.filter(category__name=cat_name)
#     context = {'posts': posts}
#     return render(request,'blog/blog-home.html',context)




########################################################### test

def test(request):
    # posts = post.objects.all()
#     posts = post.objects.filter(pk=pid)
#     # posts = post.objects.get(id=pid)
#     # posts = get_object_or_404(post,pk=pid)  #posts = get_object_or_404(name of class , name=pid)
#     if not posts.exists():
#         raise Http404("Post not found")
    # context = {'posts': posts}
    return render(request,'test.html')

