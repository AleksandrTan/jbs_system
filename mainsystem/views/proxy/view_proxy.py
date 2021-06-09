from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from django.views.generic.list import ListView

from mainsystem.views.basepage import BaseAdminView
from mainsystem.models import Proxy
from mainsystem.forms.proxy_form import ProxyForm
from mainsystem.modelswork.proxywork.proxy_work import ProxyWork


class ProxyPageView(BaseAdminView, ListView):
    """
    Get page for view proxy
    """
    template_name = 'proxy/proxy_view.html'
    model = Proxy
    queryset = ProxyWork.get_all_proxy()


class CreateProxy(BaseAdminView, TemplateView):
    template_name = "proxy/create_proxy.html"

    def post(self, request, *args, **kwargs):
        portal_form = ProxyForm(request.POST, request.FILES)
        if portal_form.is_valid():
            proxy = portal_form.save()
            return redirect('proxy_view')
        else:
            return render(request, "proxy/create_proxy.html", {"form": portal_form})


class EditProxy(BaseAdminView, UpdateView):
    model = Proxy
    fields = ['is_active']
    template_name = "proxy/edit_proxy.html"
    context_object_name = 'proxy'
    success_url = reverse_lazy('proxy_view')

