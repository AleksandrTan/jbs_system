from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.http import (HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect,
                         HttpResponsePermanentRedirect)
from rest_framework.response import Response


class MainIndeedView(TemplateView):
    """
    Start page
    """
    template_name = 'test/indee_auth.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")

        return response


class TestIndeedLoginView(TemplateView):
    template_name = 'test/indee_auth.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftokensdf", "8888888888888888888")
        response.set_cookie("midsdf", "333333333333333333333333333")
        response.set_cookie("rursdf", "Alex-4000")

        return response


class TestIndeedView(TemplateView):
    """
    Content page with work
    """
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
    """
    Логин
    """
    template_name = 'test/test_form.html'

    def post(self, request, *args, **kwargs):
        print(request.COOKIES, 3500, request.headers, sep="\n")
        return super(TestFormIndeedView, self).get(self, request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        response = super(TestFormIndeedView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('BID', '13500')
        response.set_cookie('VID', '13500')
        response.set_cookie('activity', '13500')
        response.set_cookie('ast_visit_at', '13500')
        response.set_cookie('last_jdp_search_rails', '13500')
        return response
