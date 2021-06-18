from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views

from mainsystem.views.startpage import MainView
from mainsystem.views.testview.testpage import (TestView, TestFormView, TestDataSave, OneRedirect, TwoRedirect)
from mainsystem.views.testview.indee_test import TestIndeeView
from mainsystem.views.botworker.create_task import CreateTaskPageView, SaveOrder, RestartOrder
from mainsystem.views.botworker.get_file import send_file
from mainsystem.views.apiworker.tasks_result import OrderFail,   OrderSuccess
from mainsystem.views.portalworker.portals import PortalsPageView, CreatePortal, EditPortal
from mainsystem.views.orders.order_view import OrdersView
from mainsystem.views.proxy.view_proxy import ProxyPageView, CreateProxy, EditProxy
from mainsystem.views.proxy.update_proxy import UpdateProxy
from mainsystem.views.statistics.statistics_view import StatisticsView
from mainsystem.views.settings.settings_view import SettingsView, CreateSettings, UpdateSettings

# ======================================= Main urls ==================================================================

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(success_url="homeadmin"), name='loginadmin'),
    path('logoutadmin/', auth_views.LogoutView.as_view(), name='logoutadmin'),
    path('', MainView.as_view(), name='homeadmin'),

    # ======================================= Orders urls ==========================================================
    re_path(r'^orders/view/(?:page/(?P<page>\d+)/)?$', OrdersView.as_view(), name="orders_view"),
    path('orders/restart/<int:pk>/', RestartOrder.as_view(), name="restart_order"),
    # ======================================= Portals urls ==========================================================
    path('portals/view/', PortalsPageView.as_view(), name="portals_view"),
    path('portals/create/', CreatePortal.as_view(), name="create_portal"),
    path('portals/edit/<int:pk>/', EditPortal.as_view(), name="edit_portal"),

    # ======================================= Bots urls ==============================================================
    path('bot/create_task/', CreateTaskPageView.as_view(), name="create_task"),
    path('bot/create/', SaveOrder.as_view(), name="save_order"),
    path('bot/get_file/', send_file, name="send_file"),
    path('api/order/<str:order_id>/fail/', OrderFail.as_view(), name="order_fail"),
    path('api/order/<str:order_id>/success/', OrderSuccess.as_view(), name="order_success"),

    # ======================================= Proxy urls ===========================================+===============
    path('proxy/view/', ProxyPageView.as_view(), name="proxy_view"),
    path('proxy/create/', CreateProxy.as_view(), name="create_proxy"),
    path('proxy/edit/<int:pk>/', EditProxy.as_view(), name="edit_proxy"),
    path('proxy/update/', UpdateProxy.as_view(), name="update_proxy"),

    # ======================================= Statistics urls =======================================================
    path('statistics/view/', StatisticsView.as_view(), name="statistics_view"),

    # ======================================= Settings urls =======================================================
    path('settings/view/', SettingsView.as_view(), name="settings_view"),
    path('settings/create/', CreateSettings.as_view(), name="create_settings"),
    path('settings/update/', UpdateSettings.as_view(), name="update_settings"),

    # ======================================= TEST urls ==============================================================
    path('testpage/', TestView.as_view(), name="test_page"),
    path('testform/', TestFormView.as_view(), name="test_form"),
    path('apply/j2r1zp6g5s3b9nk4h73/submit', TestDataSave.as_view(), name="save_form"),
    path('oneform/', OneRedirect.as_view(), name="one_form"),
    path('twoform/', TwoRedirect.as_view(), name="two_form"),
    # indee
    path('testpageindee/', TestIndeeView.as_view(), name="test_indee_page"),
]
