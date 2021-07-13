import json

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render

from mainsystem.views.basepage import BaseAdminView
from mainsystem.forms.order_form import OrderForm
from coresystem.rconnector import RabbitWorker
from mainsystem.modelswork.portal_work import PortalWork
from mainsystem.modelswork.proxywork.proxy_work import ProxyWork
from mainsystem.modelswork.order_work import OrderWork
from mainsystem.modelswork.settings_work import SettingsWork


class CreateTaskPageView(BaseAdminView, TemplateView):
    """
    Get page for add new task
    """
    template_name = 'botwork/create_task.html'

    def get_context_data(self, **kwargs):
        context = super(CreateTaskPageView, self).get_context_data()
        context["portals"] = PortalWork.get_all()
        context["proxy"] = ProxyWork.active_proxy_count()
        context["is_tab_open"] = True

        return context


class SaveOrder(BaseAdminView, CreateView):
    """
    Save new order, send task in RabbitMQ
    """

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order = order_form.save()
            # send message task for worker in RabbitMQ
            self.send_message(order)
            return redirect('orders_view')
        else:
            return render(request, 'botwork/create_task.html', {"form": order_form, "portals": PortalWork.get_all()})

    def send_message(self, order):
        rabbit_worker = RabbitWorker()
        proxy = ProxyWork.get_proxy()
        is_update_proxy = SettingsWork.is_update_proxy()
        task_data = {
            "status": True,
            "is_update_proxy": is_update_proxy,
            "target_link": order.target_link,
            "order_id": order.id,
            "file_mailing": order.file_mailing.url,
            "file_name": order.file_mailing.name.split("/")[-1],
            "user_name": order.user_name,
            "last_name": order.last_name,
            "password": order.password,
            "email": order.email,
            "login": order.login,
            "portal": order.portal.alias,
        }
        if proxy:
            p_data = {
                "proxy": {
                    "proxy_id": proxy.id,
                    "host": proxy.host_proxy,
                    "port": proxy.port_proxy,
                    "protocol": proxy.protocol_proxy,
                    "username": proxy.username_proxy,
                    "password": proxy.password_proxy
                }
            }
        else:
            p_data = {
                "proxy": {
                    "proxy_id": 0,
                    "host": '',
                    "port": '',
                    "protocol": '',
                    "username": '',
                    "password": ''
                }
            }
        p_data.update(task_data)
        message = json.dumps(p_data)
        print(message)
        rabbit_worker.sender(message)

        return True


class RestartOrder(SaveOrder):
    """
    Restart order, send task in RabbitMQ
    """
    def get(self, request, *args, **kwargs):
        print(3500)
        order = OrderWork.get_single_order(kwargs["pk"])
        if order["status"]:
            # send message task for worker in RabbitMQ
            self.send_message(order["order"])
            OrderWork.update_order_restart(kwargs["pk"])
        return redirect('orders_view')
