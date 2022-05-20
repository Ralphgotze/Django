from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post


@receiver(post_save,sender=Post)
def createProfile(sender,instance,created,**kwargs):
    if created:
        Post.objects.create(post=instance)

@receiver(post_save,sender=Post)
def saveProfile(sender,instance,created,**kwargs):
    instance.image.save()