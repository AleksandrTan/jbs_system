from django.views.generic.list import ListView
from mainsystem.views.basepage import BaseAdminView

from mainsystem.models import Order


class OrdersView(BaseAdminView, ListView):
    model = Order
    paginate_by = 15
    template_name = "orders/order_view.html"
    ordering = ["id"]

    def get_context_data(self, **kwargs):
        context = super(OrdersView, self).get_context_data()
        context["is_tab_open"] = True

        return context
