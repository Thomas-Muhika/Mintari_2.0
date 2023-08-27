from django.urls import path, re_path

from . import views

app_name = 'shop'

urlpatterns = [
    # mintarikenya.co.ke/shop/
    re_path(r'^$', views.shop_index, name='shop_index'),

    # mintarikenya.co.ke/shop/product/
    # re_path(r'^product/$', views.single_product, name='product'),

    # mintarikenya.co.ke/shop/ProdCategory
    path('<str:ProdCategory>/', views.ShopCategory.as_view(), name='shop_category'),

    path('product/<str:ProdCode>/', views.SingleProduct.as_view(), name='product'),
]