from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com/portal/
def portal_index(request):
    return render(request, 'portal/dashboard.html')


# mintarikenya.com/portal/add_stock/
def add_stock(request):
    return render(request, 'portal/add_stock.html')


# mintarikenya.com/portal/manage_stock/
def manage_stock(request):
    return render(request, 'portal/manage_stock.html')


# mintarikenya.com/portal/record_order/
def record_order(request):
    return render(request, 'portal/record_order.html')


# mintarikenya.com/portal/manage_orders/
def manage_orders(request):
    return render(request, 'portal/manage_orders.html')



