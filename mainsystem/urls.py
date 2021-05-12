from django.urls import path, include
from django.contrib.auth import views as auth_views

from mainsystem.views.startpage import MainView

# ======================================= Main urls ==================================================================

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(success_url="homeadmin"), name='loginadmin'),
    path('logoutadmin/', auth_views.LogoutView.as_view(), name='logoutadmin'),
    path('', MainView.as_view(), name='homeadmin'),
]