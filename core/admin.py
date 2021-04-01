from django.contrib import admin
from .models import Category, Product, ProductContent

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)


admin.site.register(ProductContent)
