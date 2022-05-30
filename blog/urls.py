from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.contrib import admin
from .views import (
    BlogHomePageView,
    # PostDetailView,
)

from . import views

app_name='blog'

urlpatterns = [
    path('',BlogHomePageView.as_view(),name='home'),
    path('<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('create/',views.image_upload_view,name='create-post'),

    path('<int:pk>/like/',views.AddLike.as_view(),name='like'),
    path('<int:pk>/dislike/',views.AddDislike.as_view(),name='dislike'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)