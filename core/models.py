
import uuid
from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models

# Create your models here.


def get_default_json():
    return {}


def get_default_list():
    return []


class Category(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, unique=True)
    display_position = models.IntegerField()
    image_url = models.CharField(
        max_length=255, null=True, blank=True, default='')
    bg_image = models.CharField(
        max_length=255, null=True, blank=True, default='')
    title = models.CharField(max_length=255, null=True, blank=True, default='')
    slug = models.CharField(max_length=255, null=True, blank=True, default='')
    is_archived = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    main_product = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    display_position = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(
        max_length=255, null=True, blank=True, default='')
    bg_image = models.CharField(
        max_length=255, null=True, blank=True, default='')
    title = models.CharField(max_length=255, null=True, blank=True, default='')
    slug = models.CharField(max_length=255, null=True, blank=True, default='')
    is_archived = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.name)


class ProductContent(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    landing_page_title1 = models.CharField(
        max_length=255, null=True, blank=True)
    landing_page_title2 = models.CharField(
        max_length=255, null=True, blank=True)
    landing_page_bg_text = models.CharField(
        max_length=255, null=True, blank=True)
    landing_page_image = models.CharField(
        max_length=255, null=True, blank=True, default='')
    brochure_link = models.CharField(max_length=255, null=True, blank=True)
    info_page_content_1 = models.TextField(null=True, blank=True)
    info_page_content_2 = models.TextField(null=True, blank=True)
    info_page_metrics_1 = models.JSONField(
        default=get_default_json, blank=True)
    info_page_metrics_2 = ArrayField(models.CharField(
        max_length=255), default=get_default_list, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product_content'

    def __str__(self):
        return str(self.product.name)


class Order(models.Model):
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str(self.name)
