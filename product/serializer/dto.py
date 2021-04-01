from rest_framework import serializers
from core.models import Category, Product, ProductContent


class CategoryDto(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('uuid', 'name', 'display_position', 'image_url',
                  'bg_image', 'title')


class ProductDto(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('uuid', 'main_product', 'category', 'name',
                  'display_position', 'image_url', 'bg_image', 'title')


class ProductContentDto(serializers.ModelSerializer):
    class Meta:
        model = ProductContent
        fields = ('landing_page_title', 'landing_page_image', 'brochure_link', 'info_page_content_1',
                  'info_page_content_2', 'info_page_metrics_1')
