from mainsystem.models import Proxy


class ProxyWork:

    @staticmethod
    def get_proxy():
        return Proxy.objects.filter(is_active=True).order_by("?").first()

