from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView

from mainsystem.views.basepage import BaseAdminView
from mainsystem.models import Portal
from mainsystem.forms.portal_form import PortalForm


class PortalsPageView(BaseAdminView, ListView):
    """
    Get page for view portals
    """
    template_name = 'portals/portals_view.html'
    model = Portal


class CreatePortal(BaseAdminView, TemplateView):
    template_name = "portals/create_portal.html"

    def post(self, request, *args, **kwargs):
        portal_form = PortalForm(request.POST, request.FILES)
        if portal_form.is_valid():
            order = portal_form.save()
            print(order.id)
            return redirect('portals_view')
        else:
            return render(request, "portals/create_portal.html", {"form": portal_form})


class EditPortal(BaseAdminView, UpdateView):
    model = Portal
    fields = ['is_active']
    template_name = "portals/portal_update_form.html"
    context_object_name = 'portal'
    success_url = reverse_lazy('portals_view')
