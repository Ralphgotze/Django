from django.contrib import admin
from . import models

#se agregan los posts en el admin
admin.site.register(models.Profile)
# @admin.register(models.User)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('first_name','username','email','password1')