from rest_framework.views import APIView
from rest_framework.response import Response

from mainsystem.modelswork.proxywork.proxy_work import ProxyWork


class UpdateProxy(APIView):
    """
    Issue updated proxy
    """
    def get(self, request, *args, **kwargs):
        data_response = dict()
        proxy = ProxyWork.get_proxy_update()
        if proxy:
            data_response["status"] = True
            data_response["proxy"] = proxy
        else:
            data_response["status"] = False

        return Response(data_response)
