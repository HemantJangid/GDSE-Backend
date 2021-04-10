from rest_framework.views import APIView
from core.models import Lead
from middleware.response import success, bad_request
from product.serializer.dao import LeadDao


class LeadView(APIView):

    def post(self, request):
        attributes = LeadDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        data = {}
        data.update(attributes.data)

        Lead.objects.create(**data)
        return success({}, "email send successfully", True)
