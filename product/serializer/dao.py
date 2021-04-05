from rest_framework import serializers


class OrderDao(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    product_name = serializers.CharField()
    address = serializers.CharField(
        required=False, default='', allow_blank=True)
