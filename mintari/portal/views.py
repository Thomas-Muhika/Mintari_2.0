from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com/portal/
def portal_index(request):
    return render(request, 'portal/dashboard.html')


# mintarikenya.com/portal/add_stock/
def add_stock(request):
    return render(request, 'portal/add_stock.html')



