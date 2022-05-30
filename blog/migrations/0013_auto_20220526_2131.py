# Generated by Django 3.2.6 on 2022-05-27 01:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(related_name='post_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
