from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.http import HttpResponse

from portal.models import StockCategories, Stock


# mintarikenya.com/shop
def shop_index(request):
    stock_table = Stock.objects.all()
    CategoryTable = StockCategories.objects.all()

    return render(request, 'shop/shop.html', {"StockTable": stock_table, "CategoryTable": CategoryTable})


class ShopCategory(View):
    def get(self, request, ProdCategory):
        try:
            stock_items = Stock.objects.all().filter(ProductCategory=ProdCategory)
            if len(stock_items) > 0:
                CategoryTable = StockCategories.objects.all()
                print(CategoryTable)
                return render(request, 'shop/shop.html', {"StockTable": stock_items, "CategoryTable": CategoryTable})
            else:
                return HttpResponse('No items in that category')  # TODO: create redirect on invalid link

        except:
            return HttpResponse('Activation link is invalid!')  # TODO: create redirect on invalid link


class SingleProduct(View):
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


