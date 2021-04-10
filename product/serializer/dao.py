from rest_framework import serializers


class OrderDao(serializers.Serializer):
    name = serializers.CharField()
    country = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()
    product_name = serializers.CharField()
    company_name = serializers.CharField()


class LeadDao(serializers.Serializer):
    name = serializers.CharField()
    company_name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.CharField()


class SendEmailDao(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient_list = serializers.ListField(child=serializers.CharField())
