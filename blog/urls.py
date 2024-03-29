from django.urls import path
from blog.views import *
from blog.feeds import LatestEntriesFeed
app_name="blog"

urlpatterns = [
    path('',blog_view,name="index"),
    path('<int:pid>',blog_single,name="single"),
    path('category/<str:cat_name>',blog_view,name="category"),
    path('tag/<str:tag_name>',blog_view,name="tags"),
    path('author/<str:author_username>',blog_view,name="author"),
    path('test',blog_test,name="test"),
    path('search/',blog_search,name="search"),
    path('rss/feed/', LatestEntriesFeed()),
]