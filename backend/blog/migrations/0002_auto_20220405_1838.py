# Generated by Django 3.2.6 on 2022-04-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('published',)},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.BinaryField(blank=True, editable=True, null=True),
        ),
    ]
