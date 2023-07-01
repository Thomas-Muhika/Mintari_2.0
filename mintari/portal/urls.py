from django.urls import path, re_path

from . import views

app_name = 'portal'

urlpatterns = [
    # mintarikenya.co.ke/portal/
    re_path(r'^$', views.portal_index, name='portal_index'),

    # mintarikenya.co.ke/portal/add_stock/
    re_path(r'^add_stock/$', views.add_stock, name='add_stock'),

]