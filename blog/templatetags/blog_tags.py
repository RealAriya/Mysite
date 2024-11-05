from django import template
from blog.models import post
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