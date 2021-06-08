from mainsystem.models import Proxy


class ProxyWork:

    @staticmethod
    def get_proxy_id(proxy_id):
        return Proxy.objects.filter(pk=proxy_id).get()

    @staticmethod
    def get_proxy():
        return Proxy.objects.filter(is_active=True).order_by("?").first()

    @staticmethod
    def active_proxy_count():
        return Proxy.objects.filter(is_active=True).count()

    @staticmethod
    def get_proxy_update(proxy_id) -> tuple:
        proxy = Proxy.objects.filter(is_active=True).exclude(pk=proxy_id).order_by("?").first()
        if proxy.username_proxy and proxy.password_proxy:
            return proxy.id, proxy.protocol_proxy + "://" + proxy.username_proxy + ":" + proxy.password_proxy + "@" +\
                   proxy.host_proxy + ":" + str(proxy.port_proxy)
        else:
            return proxy.id, proxy.protocol_proxy + "://" + proxy.host_proxy + ":" + str(proxy.port_proxy)

    @staticmethod
    def update_request_fail(proxy_id):
        proxy = ProxyWork.get_proxy_id(proxy_id)
        proxy.fail_request_proxy = proxy.fail_request_proxy + 1
        proxy.save()
