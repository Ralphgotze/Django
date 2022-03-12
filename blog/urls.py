from importlib import import_module
from unicodedata import name
from django.urls import  path
from .views import BlogListView
from .views import BlogCreateView, BlogListView

app_name="blog"

urlpatterns = [
    path('',BlogListView.as_view(), name="home"),
    path('create/',BlogCreateView.as_view(), name="home")
]