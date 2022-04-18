from django.contrib import admin
from . import models

@admin.register(models.User)
class Users(admin.ModelAdmin):
    list_display = ('id','name','email','password')
    search_fields = ('name','email','password')
