from mainsystem.models import Portal
from mainsystem.modelswork.order_work import OrderWork


class PortalWork:

    @staticmethod
    def get_stat_portals() -> list:
        """
        Return statistics for portals list
        :return: dict
        """
        data: list = list()
        portals = Portal.objects.all()
        for portal in portals:
            portal_data = dict()
            portal_data["portal_name"] = portal.name
            portal_data.update(OrderWork.stat_orders_portal(portal.id))
            data.append(portal_data)

        return data

    @staticmethod
    def get_all():
        return Portal.objects.filter(is_active=True).all()

    @staticmethod
    def get_count():
        return Portal.objects.count()
