# Generated by Django 3.2.6 on 2022-05-21 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/profile-img/default.png', null=True, upload_to='profile-img'),
        ),
    ]
