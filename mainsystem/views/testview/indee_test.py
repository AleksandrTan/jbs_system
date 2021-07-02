from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from rest_framework.status import HTTP_200_OK

from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect,
                         HttpResponsePermanentRedirect)
from rest_framework.response import Response


class TestIndeedLoginView(TemplateView):
    template_name = 'test/indee_auth.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 6000)
        response = TemplateResponse(request, self.template_name, {})
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        # response.set_cookie("rur", "Alex-4000")

        return response


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


class TestFormIndeedView(TemplateView):
    template_name = 'test/test_form.html'

    def get(self, request, *args, **kwargs):
        return super(TestFormIndeedView, self).get(self, request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super(TestFormIndeedView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('BID', '13500')
        response.set_cookie('VID', '13500')
        response.set_cookie('activity', '13500')
        response.set_cookie('ast_visit_at', '13500')
        response.set_cookie('last_jdp_search_rails', '13500')
        return response
