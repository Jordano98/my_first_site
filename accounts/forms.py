from django import forms
from django.contrib.auth.forms import UserCreationForm

class my_UserCreationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        fields=['username','email','password','password2']
