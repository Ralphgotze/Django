from django.contrib import admin
from django.urls import path,include
from .views import (
    HomePageView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomePageView.as_view(),name='Home'),
    path('blog/', include('blog.urls',namespace='blog')),
    path('accounts/', include('users.urls',namespace='users')),
    path('image/', include('image.urls',namespace='image')),
]