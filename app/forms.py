from django import forms
from . models import blog

class blog_form(forms.ModelForm):
    class Meta:
        model=blog
        fields="__all__"

title=forms.CharField(widget=forms.TextInput({"Placeholder":"Enter your title"}))
content=forms.CharField(widget=forms.TextInput({"Placeholder":"Write your content"}))
image=forms.ImageField()
date=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))