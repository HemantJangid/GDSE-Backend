from django.conf.urls import url
from product.view.v1.category import CategoryListView
from product.view.v1.vehicle import ProductVehicleListView, ProductContentView, ProductImagesView
from product.view.v1.vehicle import CategoryWiseVehicleListView
from product.view.v1.send_mail import SendMailView
from product.view.v1.order import OrderView
from product.view.v1.lead import LeadView
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
    url(r'^v1/send-mail', SendMailView.as_view()),
    url(r'^v1/order', OrderView.as_view()),
    url(r'^v1/lead', LeadView.as_view()),

]
