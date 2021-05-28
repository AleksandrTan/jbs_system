from django.views.generic import TemplateView


class TestView(TemplateView):
    template_name = 'test/test1.html'


class TestFormView(TemplateView):
    template_name = 'test/test_form.html'
