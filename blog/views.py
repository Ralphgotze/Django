from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post,Comment
from .forms import PostCreateView,CommentForm
from django.contrib.auth.decorators import login_required

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

                # form.instance.name = request.user
                # form.instance.post = post
                # form.instance.content = request.POST

                # form.save
                comment.save()
                # comment = form.instance
                # return render(request,'blog/post-detail.html',{'post':post,'form':form,'comments':comments})
                return redirect('blog:post-detail',pk)

            context = {
                'post':post,
                'form':form,
                'comments':comments
            }
        return render(request,'blog/post-detail.html',context)
        # return redirect('blog/post-detail.html'+pk)

    
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



  
# def comment_detailview(request, pk):
    
#   if request.method == 'POST':
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         form = CommentCreateView(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentCreateView()
#     return render(request, 'blog/post-detail.html', {'comment_form': form})