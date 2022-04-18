from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)