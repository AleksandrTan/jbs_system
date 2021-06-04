from mainsystem.models import Proxy


class ProxyWork:

    @staticmethod
    def get_proxy():
        return Proxy.objects.filter(is_active=True).order_by("?").first()

    @staticmethod
    def active_proxy_count():
        return Proxy.objects.filter(is_active=True).count()

    @staticmethod
    def get_proxy_update():
        proxy = Proxy.objects.filter(is_active=True).order_by("?").first()
        return proxy.protocol_proxy + "://" + proxy.username_proxy + ":" + proxy.password_proxy + "@" + proxy.host_proxy + ":" + str(proxy.port_proxy)