from django import views
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .forms import PostCreateView

class BlogHomePageView(TemplateView):
    template_name='blog/index.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.Postobjects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
    
    

def image_upload_view(request):
    if request.method == 'POST':
        form = PostCreateView(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            img_obj = form.instance
            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = PostCreateView()
    return render(request, 'blog/upload-post.html', {'form': form})
