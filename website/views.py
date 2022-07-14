from tkinter import E
from django.shortcuts import render
from website.models import Contact

def index_view(request) :
    return render(request,'website/index.html')

def about_view(request):
    return render(request,"website/about.html")

def contact_view(request):
    return render(request,"website/contact.html")

def elements_view(request):
    return render(request,"website/elements.html")

def test_view(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        massage=request.POST.get('massage')
        c= Contact()
        c.name=name
        c.email=email
        c.subject=subject
        c.message=massage
        c.save()
    return render(request,"test.html")