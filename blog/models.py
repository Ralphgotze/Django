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
    image = models.ImageField(null=True,upload_to='image-post')
    published = models.DateTimeField(default=timezone.now,editable=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    status = models.CharField(max_length=20,choices=options,default='published')
    objects = models.Manager()
    Postobjects = PostObjects()

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('published',)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.PROTECT,related_name="comments")
    name = models.ForeignKey(User,on_delete=models.PROTECT)
    content = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ("publish_date",)

        def __str__(self):
            return f"comment by: {self.name}"
