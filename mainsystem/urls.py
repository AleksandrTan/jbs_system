from django.urls import path, include
from django.contrib.auth import views as auth_views

from mainsystem.views.startpage import MainView
from mainsystem.views.testpage import TestView, TestFormView
from mainsystem.views.botworker.create_task import CreateTaskView

# ======================================= Main urls ==================================================================

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(success_url="homeadmin"), name='loginadmin'),
    path('logoutadmin/', auth_views.LogoutView.as_view(), name='logoutadmin'),
    path('', MainView.as_view(), name='homeadmin'),
    path('testpage/', TestView.as_view(), name="test_page"),
    path('testform/', TestFormView.as_view(), name="test_form"),
    path('bot/create_task', CreateTaskView.as_view(), name="create_task")
]