from django import template
from blog.models import Post,Category
register= template.Library()

@register.filter
def snippet(value,arg=20):
    return value[:arg]+'...'


@register.inclusion_tag('website/website-lastest-blog-posts.html')
def blog_latestposts():
    posts=Post.objects.filter(status=1).order_by('-published_date')[:6]
    return {'posts':posts}