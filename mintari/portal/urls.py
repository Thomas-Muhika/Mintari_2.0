from django.urls import path, re_path

from . import views

app_name = 'portal'

urlpatterns = [
    # mintarikenya.co.ke/portal/
    re_path(r'^$', views.portal_index, name='portal_index'),

    # mintarikenya.co.ke/portal/calender/
    re_path(r'^calender/$', views.calender, name='calender'),

    # mintarikenya.co.ke/portal/manage_categories/
    re_path(r'^manage_categories/$', views.manage_categories, name='manage_categories'),

    # mintarikenya.co.ke/portal/add_stock/
    re_path(r'^add_stock/$', views.add_stock, name='add_stock'),

    # mintarikenya.co.ke/portal/manage_stock/
    re_path(r'^manage_stock/$', views.manage_stock, name='manage_stock'),

    # mintarikenya.co.ke/portal/record_order/
    re_path(r'^record_order/$', views.record_order, name='record_order'),
    #
    # mintarikenya.co.ke/portal/manage_orders/
    re_path(r'^manage_orders/$', views.manage_orders, name='manage_orders'),

    # delete stock
    path('delete/stock/<str:product_code>/', views.DeleteStock.as_view(), name='delete_stock'),

    # edit stock
    path('edit/stock/<str:product_code>/', views.EditStock.as_view(), name='edit_stock'),

    # delete order
    path('delete/order/<str:order_num>/', views.DeleteOrder.as_view(), name='delete_order'),

    # mintarikenya.co.ke/portal/users/tracking/
    re_path(r'^users/tracking/$', views.users_tracking, name='users_tracking'),

]