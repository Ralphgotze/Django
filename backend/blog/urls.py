from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from .views import (
    BlogHomePageView,
    PostDetailView,
    PostCreateView
)

app_name='blog'

urlpatterns = [
    path('',BlogHomePageView.as_view(),name='home'),
    path('create/',PostCreateView.as_view(),name='create-post'),
    path('<slug:slug>',PostDetailView.as_view(),name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)