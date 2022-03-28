from django.contrib import admin
from . import models #importamos los modelos de la carpeta actual


#se agregan los posts en el admin
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','title','status','slug','author')
    prepopulated_fields = {'slug': ('title',),}

#se agregan los comentarios
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','email','publish','status')
    list_filter = ('status','publish')
    search_fields = ('name','email','content')

#se agregan las categorias
admin.site.register(models.Category)