from django.urls import path, re_path

from . import views

app_name = 'shop'

urlpatterns = [
    # mintarikenya.co.ke/shop/
    re_path(r'^$', views.shop_index, name='shop_index'),

    # mintarikenya.co.ke/shop/ProdCategory
    path('<str:ProdCategory>/', views.ShopCategory.as_view(), name='shop_category'),

    # mintarikenya.co.ke/shop/product/ProdCode/
    path('product/<str:ProdCode>/', views.SingleProduct.as_view(), name='product'),

    # mintarikenya.co.ke/shop/product/wishlist/product_code/
    path('product/wishlist/<str:product_code>/', views.WishlistProduct.as_view(), name='wishlist'),

    # mintarikenya.co.ke/shop/checkout/cart
    re_path(r'^checkout/cart/$', views.cart, name='cart'),

    # mintarikenya.co.ke/shop/checkout/cart/remove/product_code/
    path('checkout/cart/remove/<str:product_code>/', views.CartRemove.as_view(), name='cart_remove'),

    # mintarikenya.co.ke/shop/checkout/cart/checkout/
    re_path(r'^checkout/cart/checkout$', views.checkout, name='checkout'),

    # mintarikenya.co.ke/shop/custom/order/
    re_path(r'^custom/order/$', views.custom_order, name='custom_order'),


]