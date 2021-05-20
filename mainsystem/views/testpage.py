from django.views.generic import TemplateView

from mainsystem.views.basepage import BaseAdminView


class TestView(TemplateView):
    template_name = 'test.html'
