import imp
from django import views
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Post


class BlogHomePageView(TemplateView):
    template_name='blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.Postobjects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template = 'blog/post-detail.html'