from django.urls import path
from website.views import index_view,about_view,contact_view,elements_view
urlpatterns = [
    path('',index_view),
    path('about',about_view),
    path('contact',contact_view)
]