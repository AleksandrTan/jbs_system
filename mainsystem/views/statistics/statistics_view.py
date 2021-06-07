from django.views.generic import TemplateView

from mainsystem.modelswork.portal_work import PortalWork
from mainsystem.modelswork.proxywork.proxy_work import ProxyWork
from mainsystem.views.basepage import BaseAdminView
from mainsystem.modelswork.order_work import OrderWork


class StatisticsView(BaseAdminView, TemplateView):
    template_name = "statistics/statistics.html"

    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data()
        context["portals_count"] = PortalWork.get_count()
        context["proxy_count"] = ProxyWork.active_proxy_count()
        context["orders_count"] = OrderWork.get_count()
        context["orders_stat_links"] = OrderWork.stat_data_links()
        context["orders_stat"] = data = OrderWork.stat_data_orders()
        print(data)

        return context
