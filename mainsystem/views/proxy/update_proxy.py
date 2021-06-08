from rest_framework.views import APIView
from rest_framework.response import Response

from mainsystem.modelswork.proxywork.proxy_work import ProxyWork


class UpdateProxy(APIView):
    """
    Issue updated proxy
    """
    def get(self, request, *args, **kwargs):
        print(request, request.GET, args, kwargs)
        data_response = dict()
        proxy = ProxyWork.get_proxy_update(request.GET["proxy_id"])
        if proxy:
            data_response["status"] = True
            data_response["proxy"] = proxy[1]
            data_response["proxy_id"] = proxy[0]
        else:
            data_response["status"] = False
        # update proxy fail count
        if request.GET["proxy_id"] != '0':
            ProxyWork.update_request_fail(request.GET["proxy_id"])

        return Response(data_response)
