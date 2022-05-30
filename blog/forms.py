from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post,Comment

class PostCreateView(forms.ModelForm,LoginRequiredMixin):
    # title = forms.CharField(label='nigga',widget=forms.CharField(attrs={'class':'a'}))
    title = forms.CharField(label='nigga',
        widget=forms.TextInput(attrs={
            'placeholder':'Title',
            # 'class':'border-2 border-rose-500'
            }
            )
        )
    

    class Meta:
        model = Post
        fields = ('title','category','content','image','status')

    def form_valid(self,form):
        if form.is_valid():
            form.instance.author = self.request.user
            return super().form_valid(form)

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
        'class':'comment-post-input',
        'rows':3,
        'paceholder':'Comment something',})
    )
    class Meta:
        model = Comment
        fields = ('content',)
    def form_valid(self,form):
        if form.is_valid():
            form.instance.name = self.request.user
            return super().form_valid(form)