from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from mainsystem.views.basepage import BaseAdminView


class CreateTaskPageView(BaseAdminView, TemplateView):
    """
    Get page for add new task
    """
    template_name = 'botwork/create_task.html'


class SaveOrder(BaseAdminView, CreateView):
    pass
