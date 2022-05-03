from django.contrib import admin
from . import models

#se agregan los posts en el admin
admin.site.register(models.Profile)
