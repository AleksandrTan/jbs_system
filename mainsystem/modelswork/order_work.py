from django.db.models import Count, Sum

from mainsystem.models import Order
from mainsystem.modelswork.proxywork.proxy_work import ProxyWork


class OrderWork:

    @staticmethod
    def stat_orders_portal(portal_id) -> dict:
        """
        Return statistics for single portal
        :param portal_id: int
        :return:
        """
        data: dict = dict()
        data["data_success_orders"] = Order.objects.filter(status_order="done", portal_id=portal_id).count()
        data["data_fail_orders"] = Order.objects.filter(status_order="fail", portal_id=portal_id).count()
        links = Order.objects.filter(portal_id=portal_id).aggregate(total=Sum('all_links'),
                                                                    total_success=Sum('send_links'),
                                                                    total_failed=Sum('fail_links'))
        data["total"] = links["total"]
        data["total_success"] = links["total_success"]
        data["total_failed"] = links["total_failed"]

        return data

    @staticmethod
    def stat_data_orders() -> tuple:
        """
        Return statistics for orders
        :return: tuple
        """
        data_success_orders = Order.objects.filter(status_order="done").count()
        data_fail_orders = Order.objects.filter(status_order="fail").count()

        return data_success_orders, data_fail_orders

    @staticmethod
    def stat_data_links() -> dict:
        data = Order.objects.aggregate(total=Sum('all_links'), total_success=Sum('send_links'),
                                       total_failed=Sum('fail_links'))

        return data

    @staticmethod
    def get_all_objects():
        return Order.objects.all()

    @staticmethod
    def get_active_orders() -> int:
        return Order.objects.filter(status=True).count()

    @staticmethod
    def get_single_order(order_id) -> dict:
        try:
            return {"status": True, "order": Order.objects.get(id=order_id)}
        except Order.DoesNotExist:
            return {"status": False}

    @staticmethod
    def update_order_fail(order_id, data):
        data_order = OrderWork.get_single_order(order_id)
        if not data_order["status"]:
            return False
        order = data_order["order"]
        order.status = False
        order.message = data["message"]
        order.status_order = "fail"
        order.save()
        # update proxy fail count
        ProxyWork.update_request_fail(data["proxy_id"])

    @staticmethod
    def update_order_success(order_id, data):
        data_order = OrderWork.get_single_order(order_id)
        if not data_order["status"]:
            return False
        order = data_order["order"]
        order.status = False
        order.status_order = "done"
        order.message = "Task completed successfully"
        order.all_links = data["all_links"]
        order.send_links = data["send_links"]
        order.fail_links = data["fail_links"]
        order.save()

    @staticmethod
    def update_order_restart(order_id):
        data_order = OrderWork.get_single_order(order_id)
        if not data_order["status"]:
            return False
        order = data_order["order"]
        order.status_order = "create"
        order.status = True
        order.message = ''
        order.all_links = 0
        order.send_links = 0
        order.fail_links = 0
        order.save()

    @staticmethod
    def get_count() -> int:
        """
        Return count all orders
        :return: int
        """
        return Order.objects.count()
