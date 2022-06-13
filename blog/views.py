import datetime
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from blog.models import full_post
# Create your views here.

def blog_view(request):
    posts=Post.objects.filter(published_date__lte = datetime.datetime.now())
    context={'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    #the connection between blog home and blog single has not settled yet
    full_posts=full_post.objects.all() #there is a database table(full_post) for complete posts and basically,it has just ID and counted view part.
    def counter ():# it can work untilwe have one post :(
        for i in full_posts :
            i.counted_views_2 +=1
            i.save()
    counter()
    context={'full_posts':full_posts}
    return render(request,'blog/blog-single.html',context)

def blog_test (request,pid) :
    post=get_object_or_404(Post, pk=pid)
    context={'post':post}
    return render(request,'test.html',context)