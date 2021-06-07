from mainsystem.models import Portal


class PortalWork:

    @staticmethod
    def get_all():
        return Portal.objects.filter(is_active=True).all()

    @staticmethod
    def get_count():
        return Portal.objects.count()
