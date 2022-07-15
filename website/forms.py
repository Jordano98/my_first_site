from django import forms

class NameForm(forms.Form):
    name=forms.CharField(label='your name',max_length=255)
    email=forms.EmailField()
    subject=forms.CharField(max_length=255)
    massage=forms.CharField(widget=forms.Textarea)