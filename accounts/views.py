from accounts.forms import my_UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('/')
        form=AuthenticationForm()#this is really neccessary item for rendring template completely fine
        context={'form':form}
        return render (request,'accounts/login.html',context)
    else:
        return redirect('/')

@login_required(login_url='/accounts/login')
def logout_view(request):
    #if request.user.is_authenticated:
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form=my_UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')
        form=my_UserCreationForm()
        context={'form':form}
        return render (request,'accounts/signup.html',context)
    else:
        return redirect('/')

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})
# Create your views here.
