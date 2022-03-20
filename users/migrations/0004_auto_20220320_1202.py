# Generated by Django 3.2.6 on 2022-03-20 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_website_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('name', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('N', 'Not Reviewed'), ('R', 'Reviewed'), ('A', 'Accepted'), ('E', 'Error')], max_length=1),
        ),
    ]
