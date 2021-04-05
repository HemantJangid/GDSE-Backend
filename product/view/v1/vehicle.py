import uuid
from rest_framework.views import APIView
from core.models import Product, Category, ProductContent
from middleware.response import success
from product.serializer.dto import ProductDto, ProductContentDto


class ProductVehicleListView(APIView):
    def get(self, request):
        products = Product.objects.filter(
            is_archived=False).order_by('name').all()
        payload = {
            'products': ProductDto(products, many=True).data
        }
        return success(payload, 'products fetched successfully', True)


class ProductContentView(APIView):
    def get(self, request, product_id):
        query = {'is_archived': False}
        if is_valid_uuid(product_id):
            query["uuid"] = product_id
        else:
            query["slug"] = product_id
        product = Product.objects.filter(**query).first()
        if not product:
            return success({}, "invalid product id", False)

        content = ProductContent.objects.filter(product=product).first()
        if not content:
            return success({}, "no content is present", False)

        return success(ProductContentDto(content).data, "details fetched successfully", True)


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
