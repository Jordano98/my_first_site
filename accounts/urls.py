from django.urls import path
from . import views
from accounts.views import password_reset_request
#from django.contrib.auth import views as auth_views

app_name='accounts'

urlpatterns=[
    path('login',views.login_view,name='login'),
    path('signup',views.signup_view,name='signup'),
    path('logout',views.logout_view,name='logout'),
    path("password_reset", password_reset_request, name="password_reset"),
    #path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    #path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    #path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'), 
    #'''why these urls did not work here??'''
]
