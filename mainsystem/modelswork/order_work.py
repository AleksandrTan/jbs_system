from django.db import models
from mainsystem.models import Order


class OrderWork:

    @staticmethod
    def get_single_order(order_id):
        print(order_id)
        try:
            return {"status": True, "order": Order.objects.get(id=order_id)}
        except Order.DoesNotExist:
            return {"status": False}

    @staticmethod
    def update_order(order_id, data):
        data_order = OrderWork.get_single_order(order_id)
        if not data_order["status"]:
            print(3500)
            return False
        print(4000)
        order = data_order["order"]
        order.status = data["status"]
        order.save()
