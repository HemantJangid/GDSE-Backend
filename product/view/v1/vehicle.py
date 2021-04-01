import uuid
from rest_framework.views import APIView
from core.models import Product, Category
from middleware.response import success
from product.serializer.dto import ProductDto


class ProductVehicleListView(APIView):
    def get(self, request):
        products = Product.objects.filter(
            is_archived=False).order_by('name').all()
        payload = {
            'products': ProductDto(products, many=True).data
        }
        return success(payload, 'products fetched successfully', True)


class CategoryWiseVehicleListView(APIView):
    def get(self, request, category_id):
        query = {'is_archived': False}

        if is_valid_uuid(category_id):
            query["uuid"] = category_id
        else:
            query["slug"] = category_id

        category = Category.objects.filter(**query).order_by('name').first()
        if not category:
            return success({}, "invalid category id", False)

        products = Product.objects.filter(
            category=category)

        if not products:
            return success({}, "no products in this category", False)

        payload = {
            'products': ProductDto(products, many=True).data
        }
        return success(payload, 'products fetched successfully', True)


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False
