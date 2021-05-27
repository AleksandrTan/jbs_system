from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render

from mainsystem.views.basepage import BaseAdminView
from mainsystem.forms.order_form import OrderForm


class CreateTaskPageView(BaseAdminView, TemplateView):
    """
    Get page for add new task
    """
    template_name = 'botwork/create_task.html'


class SaveOrder(BaseAdminView, CreateView):

    def post(self, request, *args, **kwargs):
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save()
            return redirect('homeadmin')
        else:
            return render(request, 'botwork/create_task.html', {"form": order_form})
