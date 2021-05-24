from django.views.generic import TemplateView

from mainsystem.views.basepage import BaseAdminView


class TestView(TemplateView):
    template_name = 'test1.html'


class TestFormView(TemplateView):
    template_name = 'test_form.html'
