from django.conf.urls import url
from product.view.v1.category import CategoryListView
from product.view.v1.vehicle import ProductVehicleListView
from product.view.v1.vehicle import CategoryWiseVehicleListView
# from product.mine.v1.vehicle import news

urlpatterns = [
    url(r'^v1/product/vehicle/list$', ProductVehicleListView.as_view()),
    url(r'^v1/product/category/list$', CategoryListView.as_view()),
    url(r'^v1/product/category/(?P<category_id>[\w\-]+)/vehicle/list$',
        CategoryWiseVehicleListView.as_view()),

]
