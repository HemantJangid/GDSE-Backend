from django.contrib import admin
from .models import Category, Product, ProductContent
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(ProductContent)
class ProductContentAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass
