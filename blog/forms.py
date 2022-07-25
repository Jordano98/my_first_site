from django import forms
from blog.models import Comment

class commentform(forms.ModelForm):

    class Meta :
        model=Comment
        fields= ['post','name','email','subject','massage']