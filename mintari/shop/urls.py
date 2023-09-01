from django.urls import path, re_path

from . import views

app_name = 'shop'

urlpatterns = [
    # mintarikenya.co.ke/shop/
    re_path(r'^$', views.shop_index, name='shop_index'),

    # mintarikenya.co.ke/shop/ProdCategory
    path('<str:ProdCategory>/', views.ShopCategory.as_view(), name='shop_category'),

    # mintarikenya.co.ke/shop/ProdCode
    path('product/<str:ProdCode>/', views.SingleProduct.as_view(), name='product'),

    # mintarikenya.co.ke/shop/product_code
    path('product/wishlist/<str:product_code>/', views.WishlistProduct.as_view(), name='wishlist'),

    # mintarikenya.co.ke/shop/cart
    re_path(r'^checkout/cart/$', views.cart, name='cart'),

    # mintarikenya.co.ke/shop/cart/remove_item
    path('checkout/cart/remove/<str:product_code>/', views.CartRemove.as_view(), name='cart_remove'),

    re_path(r'^checkout/cart/checkout$', views.checkout, name='checkout'),


]