from datetime import datetime
from tkinter.tix import Tree
from unittest.util import _MAX_LENGTH
from django.db import models


class User(models.Model):
    fisrt_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cars = models.ManyToManyField('Car',verbose_name="los carros del usuario")

STATUS_CHOICES = {
    ('R', 'Reviewed'),
    ('N', 'Not Reviewed'),
    ('E', 'Error'),
    ('A', 'Accepted')
}

class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    relase_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def was_relased_last_week(self):
        if self.relase_date < datetime.date(2020,6,6):
            return "Yeah"
    @property
    def get_full_name(self):
        return "Este es el nombre de la pagina: {name}"

class Car(models.Model):
    name = models.CharField(max_length=40,primary_key=True)