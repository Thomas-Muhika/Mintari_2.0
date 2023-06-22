from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com/shop
def shop_index(request):
    return render(request, 'shop/shop.html')
