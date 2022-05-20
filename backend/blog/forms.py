from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class PostCreateView(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','content','image','status')

    def form_valid(self,form):
        if form.is_valid():
            form.instance.author = self.request.user
            return super().form_valid(form)