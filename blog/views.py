from django.db.models.functions import Now
from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.

def blog_view(request):
    posts=Post.objects.filter(published_date__lte =Now())
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    post=get_object_or_404(Post, pk=pid)
    def counter ():
        post.counted_views +=1
        post.save()
    counter()
    context={'post':post}
    return render(request,'blog/blog-single.html',context)

def blog_test (request,pid) :
    post=get_object_or_404(Post, pk=pid)
    context={'post':post}
    return render(request,'test.html',context)