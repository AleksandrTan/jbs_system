from mainsystem.models import Portal


class PortalWork:

    @staticmethod
    def get_all():
        portals = Portal.objects.filter(is_active=True).all()
        print(portals)
        return portals
