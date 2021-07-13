from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN


class MainGlassView(TemplateView):
    """
    Start page
    """
    template_name = 'test/glass_start_link.html'

    def get(self, request, *args, **kwargs):
        print(request.COOKIES, 3500)
        response = TemplateResponse(request, self.template_name, {}, status=HTTP_200_OK)
        response.set_cookie("csrftoken", "8888888888888888888")
        response.set_cookie("mid", "333333333333333333333333333")
        response.set_cookie("rur", "Alex-4000")

        return response