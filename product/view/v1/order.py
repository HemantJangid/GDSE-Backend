from rest_framework.views import APIView
from core.models import Order
from middleware.response import success, bad_request
from product.serializer.dao import OrderDao


class OrderView(APIView):

    def post(self, request):
        attributes = OrderDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        data = {}
        data.update(attributes.data)

        Order.objects.create(**data)
        return success({}, "email send successfully", True)
