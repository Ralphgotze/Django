from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

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
    image = models.ImageField(null=True,blank=True,)
    slug = models.SlugField(max_length=255,unique_for_date='published',null=False,unique=True,default=title,editable=False)
    published = models.DateTimeField(default=timezone.now,editable=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=20,choices=options,default='draft')
    objects = models.Manager()
    Postobjects = PostObjects()



    

    def __str__(self):
        return self.title
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
