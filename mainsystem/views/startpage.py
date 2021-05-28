from django.views.generic import TemplateView

from mainsystem.views.basepage import BaseAdminView


class MainView(BaseAdminView, TemplateView):
    """
    Main page admin
    """
    template_name = 'mainpage/mainpage.html'
