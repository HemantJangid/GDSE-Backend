from django.conf.urls import url
from product.view.v1.category import CategoryListView
from product.view.v1.vehicle import ProductVehicleListView, ProductContentView, ProductImagesView
from product.view.v1.vehicle import CategoryWiseVehicleListView
# from product.mine.v1.vehicle import news

urlpatterns = [
    url(r'^v1/product/list$', ProductVehicleListView.as_view()),
    url(r'^v1/category/list$', CategoryListView.as_view()),
    url(r'^v1/category/(?P<category_id>[\w\-]+)/product/list$',
        CategoryWiseVehicleListView.as_view()),
    url(r'^v1/product/(?P<product_id>[\w\-]+)/info$',
        ProductContentView.as_view()),
    url(r'^v1/product/(?P<product_id>[\w\-]+)/images$',
        ProductImagesView.as_view()),
]
