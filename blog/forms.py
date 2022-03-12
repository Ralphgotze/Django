from django import forms

from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        models=Post
        fields=('title','content')