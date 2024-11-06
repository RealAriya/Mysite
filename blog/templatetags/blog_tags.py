from django import template
from blog.models import post, Category
from django.template.defaultfilters import stringfilter
register = template.Library()


@register.simple_tag(name='totalposts')

def sum():
    posts = post.objects.filter(status=1).count()
    return posts
    
@register.filter
@stringfilter
def lower(value):
    return value.lower()

@register.inclusion_tag('blog/blog-latest.html')
def latestposts():
    postss = post.objects.filter(status=1).order_by('-published_date')[:]
    return {'postss':postss}


@register.inclusion_tag('blog/blog-category.html')
def postcategories():
    postss = post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=postss.filter(category=name).count()

    return {'categories':cat_dict}