from rest_framework.views import APIView
from rest_framework.response import Response

from mainsystem.modelswork.order_work import OrderWork


class OrderFail(APIView):
    def post(self, request, *args, **kwargs):
        data_response = dict()
        OrderWork.update_order(kwargs["order_id"], request.data)

        data_response["status"] = True

        return Response(data_response, headers={'Cache-Control': 'no-cache'})
