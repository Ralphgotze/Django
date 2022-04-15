from genericpath import exists
from django import views
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from requests import request
from .models import Post



class BlogHomePageView(LoginRequiredMixin,TemplateView):
    template_name='blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.Postobjects.all()
        return context



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.filter(slug=self.kwargs.get('slug'))
        return context

# def image_upload_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = Post.image(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = Post()
#     return render(request, 'blog/index.html', {'form': form})


def UserView(request):
    return render(request,'blog/index_logged.html')