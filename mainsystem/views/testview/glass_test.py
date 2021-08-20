from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


class MainGlassView(TemplateView):
    """
    Start page
    """
    template_name = 'test/glass_start_link.html'
    # template_name = 'test/indee_main.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")
        response.set_cookie("_csrftoken", "8888888888888888888")
        response.set_cookie("__csrftoken", "8888888888888888888")
        response.set_cookie("___csrftoken", "8888888888888888888")

        return response


class JobGlassView(TemplateView):
    """
    Job page(click Easy Apply button)
    """
    template_name = 'test/glass_job_link1.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")
        response.set_cookie("_csrftoken", "8888888888888888888")
        response.set_cookie("__csrftoken", "8888888888888888888")
        response.set_cookie("___csrftoken", "8888888888888888888")

        return response


class FormJobGlassView(TemplateView):
    """
    GET Form page
    """
    template_name = 'test/glass_form_link1.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")
        response.set_cookie("_csrftoken", "8888888888888888888")
        response.set_cookie("__csrftoken", "8888888888888888888")
        response.set_cookie("___csrftoken", "8888888888888888888")

        return response