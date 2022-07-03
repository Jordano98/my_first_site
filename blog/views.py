from django.db.models.functions import Now
from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request):
    posts=Post.objects.filter(published_date__lte =Now(),status=1)
    context={'posts':posts }
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    posts=Post.objects.filter(published_date__lte =Now(),status=1)
    len_posts=len(posts)
    post=get_object_or_404(Post, pk=pid,published_date__lte =Now(),status=1)
    def counter ():
        post.counted_views +=1
        post.save()
    counter()
    context={'post':post ,'len_posts':len_posts}
    return render(request,'blog/blog-single.html',context)

'''def blog_test (request,pid) :
    post=get_object_or_404(Post, pk=pid)
    context={'post':post}
    return render(request,'test.html',context)'''