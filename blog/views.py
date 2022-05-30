from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post,Comment
from .forms import PostCreateView,CommentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

class BlogHomePageView(TemplateView):
    template_name='blog/index.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.Postobjects.all()
        return context


class PostDetailView(LoginRequiredMixin,View):
    def get(self,request,pk,*args,**kwargs):
        
        post = Post.objects.get(pk=pk)
        form = CommentForm()

        comments=Comment.objects.filter(post=post).order_by('publish_date')

        context = {
            'post':post,
            'form':form,
            'comments':comments
        }
        return render(request,'blog/post-detail.html',context)
        
    def post(self,request,pk,*args,**kwargs):
        if request.method == 'POST':
            post = Post.objects.get(pk=pk)
            form = CommentForm(request.POST)
            comments=Comment.objects.filter(post=post).order_by('publish_date')

            if form.is_valid():
                comment = form.save(commit=False)
                comment.name = request.user
                comment.post = post
                comment.save()
                # comment.save()
                return redirect('blog:post-detail',pk)

            context = {
                'post':post,
                'form':form,
                'comments':comments
            }
        return render(request,'blog/post-detail.html',context)

    
@login_required
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



  


class AddLike(LoginRequiredMixin,View):
    def post(self,request,pk,*args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break
        
            if dislike:
                post.dislikes.remove(request.user)


        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)
            post.dislikes.remove(request.user)

        if is_like:
            post.likes.remove(request.user)

        
        return redirect('blog:post-detail',pk)

class AddDislike(LoginRequiredMixin,View):
    def post(self,request,pk,*args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)
            post.likes.remove(request.user)
        
        if is_dislike:
            post.dislikes.remove(request.user)
        
        return redirect('blog:post-detail',pk)