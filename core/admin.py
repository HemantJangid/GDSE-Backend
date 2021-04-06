from django.contrib import admin
from .models import Category, Product, ProductContent, ProductImage
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Register your models here.


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    readonly_fields = ('uuid',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductContent)
class ProductContentAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass
