from django.urls import path, re_path

from . import views

app_name = 'portal'

urlpatterns = [
    # mintarikenya.co.ke/portal/
    re_path(r'^$', views.portal_index, name='portal_index'),

    # mintarikenya.co.ke/portal/add_stock/
    re_path(r'^add_stock/$', views.add_stock, name='add_stock'),

    # mintarikenya.co.ke/portal/manage_stock/
    re_path(r'^manage_stock/$', views.manage_stock, name='manage_stock'),

    # mintarikenya.co.ke/portal/record_order/
    re_path(r'^record_order/$', views.record_order, name='record_order'),
    #
    # mintarikenya.co.ke/portal/manage_orders/
    re_path(r'^manage_orders/$', views.manage_orders, name='manage_orders'),

]