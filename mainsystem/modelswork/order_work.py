from mainsystem.models import Order


class OrderWork:

    @staticmethod
    def get_single_order(order_id):
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
        order.status = data["status"]
        order.message = data["message"]
        order.save()

    @staticmethod
    def update_order_success(order_id, data):
        data_order = OrderWork.get_single_order(order_id)
        if not data_order["status"]:
            return False
        order = data_order["order"]
        order.status = data["status"]
        order.message = data["message"]
        order.save()
