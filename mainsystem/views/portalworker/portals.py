from django.views.generic.list import ListView
from django.views.generic import TemplateView

from mainsystem.views.basepage import BaseAdminView
from mainsystem.models import Portal


class PortalsPageView(BaseAdminView, ListView):
    """
    Get page for view portals
    """
    template_name = 'portals/portals_view.html'
    model = Portal


class CreatePortal(BaseAdminView, TemplateView):
    template_name = "portals/create.html"
