from django.shortcuts import render, redirect
from portal.models import RecordOrder, StockCategories, Stock
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com/portal/
def portal_index(request):
    return render(request, 'portal/dashboard.html')


def calender(request):
    return render(request, 'portal/calender.html')


def manage_categories(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'AddCategory':

            StockCategories.objects.create(
                category=request.POST['CategoryName'],
            )

    categories_table = StockCategories.objects.all()

    return render(request, 'portal/manage_categories.html', {"CategoriesTable": categories_table})


# mintarikenya.com/portal/add_stock/
def add_stock(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'AddStock':

            Stock.objects.create(
                ProductTitle=request.POST['ProductTitle'],
                ProductCode=request.POST['ProductSKU'],
                ProductCategory=request.POST['ProductCategory'],
                ProductWeight=request.POST['ProductWeight'],
                ProductDimension=request.POST['ProductDimension'],
                ProductPrice=request.POST['BasePrice'],
                ShortDescription=request.POST['ShortDescription'],
                DetailedDescription=request.POST['DetailedDescription'],
                ProductBaseImage=request.POST['MainImage'],
                ProductImages=request.POST['AdditionalImages'],
            )

    return render(request, 'portal/add_stock.html')


# mintarikenya.com/portal/manage_stock/
def manage_stock(request):
    stock_table = Stock.objects.all()
    return render(request, 'portal/manage_stock.html', {"StockTable": stock_table})


# mintarikenya.com/portal/record_order/
def record_order(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'RecordOrder':

            RecordOrder.objects.create(
                FirstName=request.POST['FirstName'],
                LastName=request.POST['LastName'],
                Email=request.POST['Email'],
                Phone=request.POST['PhoneNumber'],
                ProductTitle=request.POST['ProductTitle'],
                DepositPaid=request.POST['DepositPaid'],
            )

    return render(request, 'portal/record_order.html')


# mintarikenya.com/portal/manage_orders/
def manage_orders(request):
    records_table = RecordOrder.objects.all()

    # print(RecordsTable[0].LastName)

    return render(request, "portal/manage_orders.html", {"RecordsTable": records_table})


