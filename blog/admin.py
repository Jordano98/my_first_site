from django.contrib import admin
from blog.models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display = ('title' ,'author','counted_views','status','published_date','created_date')
    list_filter = ('status','author')
    #ordering= ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ['content']
admin.site.register(Post,PostAdmin)


admin.site.register(Category)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display = ('post','name','email','approach','created_date')
    list_filter = ('post','approach')
    search_fields = ['name','post']
admin.site.register(Comment,CommentAdmin)