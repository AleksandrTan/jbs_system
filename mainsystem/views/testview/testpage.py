from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden)


class TestView(TemplateView):
    template_name = 'test/test1.html'

    # def get(self, request, *args, **kwargs):
    #     return HttpResponseForbidden()


class TestFormView(TemplateView):
    template_name = 'test/test_form.html'

    def get(self, request, *args, **kwargs):
        return HttpResponseBadRequest(content="Fail")
