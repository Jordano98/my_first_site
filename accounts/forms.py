from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class my_UserCreationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta :
        model=User
        fields=['username','email','password','password2']

    def save (self, commite=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commite:
            user.save()
        return user
