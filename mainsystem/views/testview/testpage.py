from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from mainsystem.forms.test_form import TestForm
from django.http import HttpResponse
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect,
                         HttpResponsePermanentRedirect)


class TestView(TemplateView):
    template_name = 'test/test1.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        return super(TestView, self).get(self, request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super(TestView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('BID', '3500')
        response.set_cookie('VID', '3500')
        response.set_cookie('activity', '3500')
        response.set_cookie('ast_visit_at', '3500')
        response.set_cookie('last_jdp_search_rails', '3500')
        return response
    # def get(self, request, *args, **kwargs):
    #     return HttpResponseForbidden()


class TestFormView(TemplateView):
    template_name = 'test/test_form.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        return super(TestFormView, self).get(self, request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super(TestFormView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('BID', '13500')
        response.set_cookie('VID', '13500')
        response.set_cookie('activity', '13500')
        response.set_cookie('ast_visit_at', '13500')
        response.set_cookie('last_jdp_search_rails', '13500')
        return response

    #
    # def get(self, request, *args, **kwargs):
    #     return HttpResponseBadRequest(content="Fail")


class TestDataSave(CreateView):
    def post(self, request, *args, **kwargs):
        print(request.headers)
        order_form = TestForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save()
            return HttpResponseRedirect("http://127.0.0.1:8000/mainsystem/oneform/")
        else:
            print(order_form.errors)
            return HttpResponseBadRequest(content="DFail")


class OneRedirect(View):
    def post(self, request, *args, **kwargs):
        return HttpResponsePermanentRedirect("http://127.0.0.1:8000/mainsystem/twoform/")

    def get(self, request, *args, **kwargs):
        return HttpResponsePermanentRedirect("http://127.0.0.1:8000/mainsystem/twoform/")


class TwoRedirect(TemplateView):
    template_name = 'test/test_form.html'
