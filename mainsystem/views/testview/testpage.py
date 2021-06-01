from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from mainsystem.forms.test_form import TestForm
from django.http import HttpResponse
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect)


class TestView(TemplateView):
    template_name = 'test/test1.html'

    # def get(self, request, *args, **kwargs):
    #     return HttpResponseForbidden()


class TestFormView(TemplateView):
    template_name = 'test/test_form.html'
    #
    # def get(self, request, *args, **kwargs):
    #     return HttpResponseBadRequest(content="Fail")


class TestDataSave(CreateView):
    def post(self, request, *args, **kwargs):
        print(request.headers)
        order_form = TestForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save()
            return HttpResponse()
        else:
            print(order_form.errors)
            return HttpResponseBadRequest(content="DFail")
