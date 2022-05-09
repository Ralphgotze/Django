from django import views
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post





class BlogHomePageView(TemplateView):
    template_name='blog/index.html'

    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.Postobjects.all()
        return context


    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'slug':self.slug})



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.filter(slug=self.kwargs.get('slug'))
        return context

    
    def get_absolute_url(self):
        return reverse('blog/post-detail.html',kwargs={'slug':self.slug})



class PostCreateView(CreateView):
    model = Post
    fields = ['title','category','content','image','status']
    
    template_name = 'blog/upload-post.html'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('blog/post-detail.html',kwargs={'slug':self.slug})

    # def get_absolute_url(self):
    # kwargs = {
    #     'pk': self.id,
    #     'slug': self.slug
    # }
    # return reverse('article-pk-slug-detail', kwargs=kwargs)