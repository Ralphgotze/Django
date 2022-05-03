from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name='account'

urlpatterns = [
    # path('dashboard/',views.dashboard,name="dashboard"),
    # path('login/',views.login,name="login"),
    path('register/',views.register,name="register"),
    path('profile/',views.profile,name="profile"),
    path('login/',auth_views.LoginView.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(),name="logout"),
    # path('logout/',views.logout,name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)