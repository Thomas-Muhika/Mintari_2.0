from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Count
from django.conf import settings
from django.views import View

from portal.models import StockCategories, Stock, WishList, Cart, Order


# mintarikenya.com/shop
def shop_index(request):
    stock_table = Stock.objects.all()
    CategoryTable = StockCategories.objects.all()

    # top 3 products in wishlist

    wishlist = WishList.objects.values_list('ProductCode').annotate(truck_count=Count('ProductCode')).order_by('-truck_count')
    wishlist_append = []
    n=0
    try:
        for data in wishlist:
            stock_items = stock_table.filter(ProductCode=data[0])[0]
            wishlist_append.append(stock_items)
            n+=1
            if n == 3:
                break
    except:
        pass

    return render(request, 'shop/shop.html', {"StockTable": stock_table, "CategoryTable": CategoryTable, "wishlist_append": wishlist_append})


class ShopCategory(View):
    def get(self, request, ProdCategory):

        stock_table = Stock.objects.all()
        CategoryTable = StockCategories.objects.all()

        wishlist = WishList.objects.values_list('ProductCode').annotate(truck_count=Count('ProductCode')).order_by('-truck_count')
        wishlist_append = []
        n = 0
        for data in wishlist:
            stock_items = stock_table.filter(ProductCode=data[0])[0]
            wishlist_append.append(stock_items)
            n += 1
            if n == 3:
                break

        try:
            stock_items = stock_table.filter(ProductCategory=ProdCategory)
            if len(stock_items) > 0:
                return render(request, 'shop/shop.html', {"StockTable": stock_items, "CategoryTable": CategoryTable})
            else:
                messages.error(request, 'Category ' + str(ProdCategory) + ' is currently missing, Explore other products', extra_tags="error")
                return render(request, 'shop/shop.html', {"StockTable": stock_table, "CategoryTable": CategoryTable, "wishlist_append": wishlist_append})

        except:
            messages.error(request, 'Product Category Invalid: Explore other similar products', extra_tags="error")
            return render(request, 'shop/shop.html', {"StockTable": stock_table, "CategoryTable": CategoryTable})


class SingleProduct(View):

    def post(self, request, ProdCode):
        try:
            stock_item = Stock.objects.all().filter(ProductCode=ProdCode)[0]
            related_items = Stock.objects.all().filter(ProductCategory=stock_item.ProductCategory)
            if len(related_items) > 4:
                related_items = related_items[:4]

            price = '{:,.2f}'.format(stock_item.ProductPrice)

            if Cart.objects.all().filter(MintariUser=request.user.username, ProductCode=ProdCode).exists():

                messages.success(request, '"' + str(Stock.objects.all().filter(ProductCode=ProdCode)[0].ProductTitle) + '" already exists in your cart')
                return render(request, 'shop/product.html',{'stock_item': stock_item, 'related_items': related_items, 'price': price})
            else:

                Cart.objects.create(
                    ProductCode=ProdCode,
                    MintariUser=request.user.username,
                )

                messages.success(request, '"' + str(Stock.objects.all().filter(ProductCode=ProdCode)[0].ProductTitle) + '" has been added to your cart')
                return render(request, 'shop/product.html', {'stock_item': stock_item, 'related_items': related_items, 'price': price})

        except:
            return HttpResponse('Activation link is invalid!')  # TODO: create redirect on invalid link

    def get(self, request, ProdCode):

        try:
            stock_item = Stock.objects.all().filter(ProductCode=ProdCode)[0]
            related_items = Stock.objects.all().filter(ProductCategory=stock_item.ProductCategory)
            if len(related_items) > 4:
                related_items = related_items[:4]

            price = '{:,.2f}'.format(stock_item.ProductPrice)
            return render(request, 'shop/product.html', {'stock_item': stock_item, 'related_items': related_items, 'price': price})

        except:
            return HttpResponse('Activation link is invalid!')  # TODO: create redirect on invalid link


class WishlistProduct(LoginRequiredMixin, View):
    login_url = "shop:shop_index"

    def get(self, request, product_code):
        try:
            stock_table = Stock.objects.all()
            CategoryTable = StockCategories.objects.all()

            wishlist = WishList.objects.values_list('ProductCode').annotate(truck_count=Count('ProductCode')).order_by('-truck_count')
            wishlist_append = []
            n = 0

            for data in wishlist:
                stock_items = stock_table.filter(ProductCode=data[0])[0]
                wishlist_append.append(stock_items)
                n += 1
                if n == 3:
                    break

            if WishList.objects.all().filter(MintariUser=request.user.username, ProductCode=product_code).exists():
                messages.info(request, str(Stock.objects.all().filter(ProductCode=product_code)[0].ProductTitle) + ' already exists in your wishlist')
                return render(request, 'shop/shop.html', {"StockTable": stock_table, "CategoryTable": CategoryTable, "wishlist_append": wishlist_append})
            else:
                WishList.objects.create(
                    ProductCode=product_code,
                    MintariUser=request.user.username,
                )

                messages.success(request, str(Stock.objects.all().filter(ProductCode=product_code)[0].ProductTitle) + ' has been added to your wishlist')
                return render(request, 'shop/shop.html', {"StockTable": stock_table, "CategoryTable": CategoryTable, "wishlist_append": wishlist_append})

        except:
            stock_table = Stock.objects.all()
            CategoryTable = StockCategories.objects.all()

            messages.error(request,'There is an error adding item to wishlist, try again')
            return render(request, 'shop/shop.html', {"StockTable": stock_table, "CategoryTable": CategoryTable, "wishlist_append": wishlist_append})


@login_required(login_url="accounts:signin")
def cart(request):
    stock_table = Stock.objects.all()
    cart_data = Cart.objects.all().filter(MintariUser=request.user.username)

    cart_append = []
    subtotal = 0
    for data in cart_data:
        cart_items = stock_table.filter(ProductCode=data.ProductCode)[0]
        cart_append.append(cart_items)

        amount = cart_items.ProductPrice
        subtotal = subtotal + amount

    with_vat = '{:,.2f}'.format(subtotal * 1.16)

    return render(request, 'shop/cart.html', {"cart_append": cart_append, "subtotal": subtotal, "withvat": with_vat})


class CartRemove(LoginRequiredMixin, View):
    login_url = "shop:shop_index"

    def get(self, request, product_code):
        entry = Cart.objects.get(ProductCode=product_code, MintariUser=request.user.username)
        entry.delete()

        return redirect('shop:cart')


def checkout(request):

    stock_table = Stock.objects.all()
    cart_data = Cart.objects.all().filter(MintariUser=request.user.username)

    cart_append = []
    items_skus = []
    subtotal = 0
    for data in cart_data:
        cart_items = stock_table.filter(ProductCode=data.ProductCode)[0]
        cart_append.append(cart_items)

        amount = cart_items.ProductPrice
        subtotal = subtotal + amount

        sku = cart_items.ProductCode
        items_skus.append(sku)

    with_vat = '{:,.2f}'.format(subtotal * 1.16)

    if request.method == 'POST':
        if request.POST.get('submit') == 'Place_order':
            Order.objects.create(
                FirstName=request.POST['billing_first_name'],
                LastName=request.POST['billing_last_name'],
                Company=request.POST['billing_company'],
                Country=request.POST['billing_country'],
                BillingAddress1=request.POST['billing_address_1'],
                BillingAddress2=request.POST['billing_address_2'],
                City=request.POST['billing_city'],
                PostCode=request.POST['billing_postcode'],
                phone_number=request.POST['billing_phone'],
                email=request.POST['billing_email'],
                products=items_skus,
                subtotal=subtotal,
                MintariUser=request.user.username,
            )
            message = get_template('shop/order_confirmation.html').render({"user_name": request.user.first_name, "email": request.POST['billing_email'], "phone": request.POST['billing_phone']})
            mail = EmailMessage('MINTARI ORDER CONFIRMATION', message, to=[request.POST['billing_email']], from_email=settings.EMAIL_HOST_USER)
            mail.content_subtype = 'html'
            mail.send()

    return render(request, 'shop/checkout.html', {"cart_append": cart_append, "subtotal": subtotal, "withvat": with_vat})

