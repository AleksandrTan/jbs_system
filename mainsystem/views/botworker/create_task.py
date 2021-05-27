from django.views.generic import TemplateView

from mainsystem.views.basepage import BaseAdminView


class CreateTaskView(BaseAdminView, TemplateView):
    template_name = 'botwork/create_task.html'
