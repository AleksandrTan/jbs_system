from django.urls import path
from django.contrib.auth import views as auth_views

from mainsystem.views.startpage import MainView
from mainsystem.views.testview.testpage import TestView, TestFormView, TestDataSave
from mainsystem.views.botworker.create_task import CreateTaskPageView, SaveOrder
from mainsystem.views.botworker.get_file import send_file
from mainsystem.views.apiworker.tasks_result import OrderFail
from mainsystem.views.portalworker.portals import PortalsPageView, CreatePortal, EditPortal

# ======================================= Main urls ==================================================================

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(success_url="homeadmin"), name='loginadmin'),
    path('logoutadmin/', auth_views.LogoutView.as_view(), name='logoutadmin'),
    path('', MainView.as_view(), name='homeadmin'),

    # ======================================= Portals urls ==========================================================
    path('portals/view/', PortalsPageView.as_view(), name="portals_view"),
    path('portals/create/', CreatePortal.as_view(), name="create_portal"),
    path('portals/edit/<int:pk>/', EditPortal.as_view(), name="edit_portal"),

    # ======================================= Bots urls ==============================================================
    path('bot/create_task/', CreateTaskPageView.as_view(), name="create_task"),
    path('bot/create/', SaveOrder.as_view(), name="save_order"),
    path('bot/get_file/', send_file, name="send_file"),
    path('api/order/<str:order_id>/fail/', OrderFail.as_view(), name="order_done"),

    # ======================================= TEST urls ==============================================================
    path('testpage/', TestView.as_view(), name="test_page"),
    path('testform/', TestFormView.as_view(), name="test_form"),
    path('apply/j2r1zp6g5s3b9nk4h73/submit', TestDataSave.as_view(), name="save_form"),
]
