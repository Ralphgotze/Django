from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect,HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
    options =(
        ('draft','Draft'),
        ('published','Published')
    )

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    content = models.TextField()
    image = models.ImageField(null=True)
    published = models.DateTimeField(default=timezone.now,editable=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=20,choices=options,default='published')
    objects = models.Manager()
    Postobjects = PostObjects()

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     super(Post, self).save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
    
    class Meta:
        ordering = ('published',)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.PROTECT,related_name="comments")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish",)

        def __str__(self):
            return f"comment by: {self.name}"

