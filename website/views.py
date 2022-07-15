from django.shortcuts import render,HttpResponse
from website.models import Contact
from website.forms import NameForm

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
        form=NameForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            subject=form.cleaned_data['subject']
            massage=form.cleaned_data['massage']
            print(name,email,subject,massage)
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
    form=NameForm()
    return render(request,"test.html",{'form':form})