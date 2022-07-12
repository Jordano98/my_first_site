from django.db.models.functions import Now
from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.

def blog_view(request,**kwargs):
    posts=Post.objects.filter(published_date__lte =Now(),status=1)
    if kwargs.get('cat_name') != None:
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts=posts.filter(author__username=kwargs['author_username'])
    context={'posts':posts }
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):

    post=get_object_or_404(Post, pk=pid,published_date__lte =Now(),status=1)
    nextpost = Post.objects.filter(created_date__gt=post.created_date).order_by('created_date').first()
    prevpost = Post.objects.filter(created_date__lt=post.created_date).order_by('created_date').last()
    
    def counter ():
        post.counted_views +=1
        post.save()
    counter()
    
    context={'post':post, 'prevpost': prevpost , 'nextpost' : nextpost}
    return render(request,'blog/blog-single.html',context)

def blog_test (request) :
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(category__name=cat_name)
    context={'posts':posts }
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts=Post.objects.filter(published_date__lte =Now(),status=1)
    if request.method == 'GET':
        #print(request.GET.get('s'))
        if x := request.GET.get('s') : #warlus operator :=
            posts=posts.filter(content__contains=x)
    context={'posts':posts }
    return render(request,'blog/blog-home.html',context)