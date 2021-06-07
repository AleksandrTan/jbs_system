from django.views.generic import TemplateView

from mainsystem.modelswork.portal_work import PortalWork
from mainsystem.modelswork.proxywork.proxy_work import ProxyWork
from mainsystem.views.basepage import BaseAdminView
from mainsystem.modelswork.order_work import OrderWork


class StatisticsView(BaseAdminView, TemplateView):
    template_name = "statistics/statistics.html"

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data()
        context["portals"] = PortalWork.get_count()
        context["proxy"] = ProxyWork.active_proxy_count()
        context["orders"] = OrderWork.get_all_orders()

        return context
