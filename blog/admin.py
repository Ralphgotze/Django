from django.contrib import admin
from . import models #importamos los modelos de la carpeta actual


#se agregan los posts en el admin
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','status','author','image')


#se agregan los comentarios
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','name','publish_date','status')
    list_filter = ('status','publish_date')
    search_fields = ('name','content')

#se agregan las categorias
admin.site.register(models.Category)
