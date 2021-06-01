from mainsystem.models import Proxy


class ProxyWork:

    @staticmethod
    def get_proxy():
        proxy = Proxy.objects.filter(is_active=True).order_by("?").first()

        return proxy
