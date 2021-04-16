
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
    image_url = models.FileField(blank=True, null=True)
    landing_image = models.FileField(blank=True, null=True)
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
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=255, unique=True)
    display_position = models.IntegerField(blank=True, null=True)
    image_url = models.FileField(blank=True, null=True)
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

    def categories(self):
        return ', '.join(str(c) for c in self.category.all())


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    image = models.FileField(blank=True, null=True)

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
    landing_page_image = models.FileField(blank=True, null=True)
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
    name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return str(self.name)


class Lead(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lead'

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    blog_title = models.CharField(max_length=255, unique=True)
    blog_image = models.FileField(blank=True, null=True)
    blog_description = models.TextField()
    blog_content = models.TextField()

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return str(self.blog_title)
