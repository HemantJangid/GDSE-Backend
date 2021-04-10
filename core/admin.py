from django.contrib import admin
from .models import Category, Product, ProductContent, ProductImage, Blog, Order, Lead
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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    search_fields = ['name', 'country']
    list_display = ('name', 'company_name', 'phone',
                    'email', 'country', 'product_name', 'created_on')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    search_fields = ['name', 'country']
    list_display = ('name', 'company_name', 'phone',
                    'email', 'created_on')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
