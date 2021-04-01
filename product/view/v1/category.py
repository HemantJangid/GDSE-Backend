from rest_framework.views import APIView
from core.models import Category
from middleware.response import success
from product.serializer.dto import CategoryDto


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.filter(
            is_archived=False).order_by('name').all()
        payload = {
            'categories': CategoryDto(categories, many=True).data
        }
        return success(payload, 'categories fetched successfully', True)
