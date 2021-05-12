from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from mainsystem.views.basepage import BaseAdminView


class MainView(BaseAdminView, TemplateView):
    template_name = 'mainpage/mainpage.html'
