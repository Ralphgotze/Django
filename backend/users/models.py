from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Tus propiedades personalizadas
    # creditos = models.PositiveIntegerField(verbose_name='creditos',
    #     default=0, 
    #     blank=True)
    pass