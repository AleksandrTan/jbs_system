import json

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render

from mainsystem.views.basepage import BaseAdminView
from mainsystem.forms.order_form import OrderForm
from coresystem.rconnector import RabbitWorker
from mainsystem.modelswork.portal_work import PortalWork


class CreateTaskPageView(BaseAdminView, TemplateView):
    """
    Get page for add new task
    """
    template_name = 'botwork/create_task.html'

    def get_context_data(self, **kwargs):
        context = super(CreateTaskPageView, self).get_context_data()
        context["portals"] = PortalWork.get_all()
        return context


class SaveOrder(BaseAdminView, CreateView):
    """
    Save new order, send task in RabbitMQ
    """
    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order = order_form.save()
            print(order.id)
            # send message task for worker in RabbitMQ
            self.send_message(order)
            return redirect('homeadmin')
        else:
            return render(request, 'botwork/create_task.html', {"form": order_form})

    def send_message(self, order):
        rabbit_worker = RabbitWorker()
        message = json.dumps(
            {
                "status": True,
                "target_link": order.target_link,
                "order_id": order.id,
                "file_mailing": order.file_mailing.url,
                "user_name": order.user_name,
                "last_name": order.last_name,
                "email": order.email,
                "proxy": {
                    "proxy_id": 1,
                    "host": "138.219.173.58",
                    "port": 0,
                    "protocol": "http",
                    "username": '2DxLL0',
                    "password": 'fwcZsa'
                }
            })

        rabbit_worker.sender(message)
