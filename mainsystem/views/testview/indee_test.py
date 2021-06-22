from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from mainsystem.forms.test_form import TestForm
from django.http import HttpResponse
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect,
                         HttpResponsePermanentRedirect)


class TestIndeedLoginView(TemplateView):
    template_name = 'test/indee_auth.html'


class TestIndeedView(TemplateView):
    template_name = 'test/indee_main.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        return super(TestIndeedView, self).get(self, request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super(TestIndeedView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('BID', '3500')
        response.set_cookie('VID', '3500')
        response.set_cookie('activity', '3500')
        response.set_cookie('ast_visit_at', '3500')
        response.set_cookie('last_jdp_search_rails', '3500')
        return response
