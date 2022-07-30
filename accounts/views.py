from django.shortcuts import render

def login_view(request):
    return (request,'accounts/login.html')

#def logout_view(request):
    #return (request,'accounts/login.html')

def signup_view(request):
    return (request,'accounts/signup.html')

# Create your views here.
