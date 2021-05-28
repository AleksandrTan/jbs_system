from django.urls import path
from django.contrib.auth import views as auth_views

from mainsystem.views.startpage import MainView
from mainsystem.views.testview.testpage import TestView, TestFormView
from mainsystem.views.botworker.create_task import CreateTaskPageView, SaveOrder
from mainsystem.views.botworker.get_file import send_file

# ======================================= Main urls ==================================================================

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(success_url="homeadmin"), name='loginadmin'),
    path('logoutadmin/', auth_views.LogoutView.as_view(), name='logoutadmin'),
    path('', MainView.as_view(), name='homeadmin'),
    path('bot/create_task/', CreateTaskPageView.as_view(), name="create_task"),
    path('bot/create/', SaveOrder.as_view(), name="save_order"),
    path('bot/get_file/', send_file, name="send_file"),

    # ======================================= TEST urls ==============================================================
    path('testpage/', TestView.as_view(), name="test_page"),
    path('testform/', TestFormView.as_view(), name="test_form"),

]
