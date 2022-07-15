from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, contactform,newsletterform

def index_view(request) :
    return render(request,'website/index.html')

def about_view(request):
    return render(request,"website/about.html")

def contact_view(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
    form=contactform()
    return render(request,"website/contact.html",{'form':form})

def newsletter_view(request):
    if request.method=='POST':
        form=newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
    form=newsletterform()
    #there is no need to rendering

def elements_view(request):
    return render(request,"website/elements.html")

def test_view(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            # name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # subject=form.cleaned_data['subject']
            # massage=form.cleaned_data['massage']
            # print(name,email,subject,massage)
            return HttpResponse('done')
            
        else:
            return HttpResponse('not valid')
        # email=request.POST.get('email')
        # subject=request.POST.get('subject')
        # massage=request.POST.get('massage')
        # c= Contact()
        # c.name=name
        # c.email=email
        # c.subject=subject
        # c.message=massage
        # c.save()
    form=contactform()
    return render(request,"test.html",{'form':form})