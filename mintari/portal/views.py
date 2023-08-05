from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from portal.models import RecordOrder, StockCategories, Stock
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com/portal/
@login_required(login_url="accounts:signup")
def portal_index(request):

    total_deposit = RecordOrder.objects.aggregate(Sum('DepositPaid'))['DepositPaid__sum']
    total_deposit = 'Ksh {:,.2f}'.format(total_deposit)

    products_sold = len(RecordOrder.objects.all())

    return render(request, 'portal/dashboard.html', {'revenue': total_deposit, 'products_sold': products_sold})


@login_required(login_url="accounts:signup")
def calender(request):
    return render(request, 'portal/calender.html')


@login_required(login_url="accounts:signup")
def manage_categories(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'AddCategory':

            StockCategories.objects.create(
                category=request.POST['CategoryName'],
            )

    categories_table = StockCategories.objects.all()

    return render(request, 'portal/manage_categories.html', {"CategoriesTable": categories_table})


# mintarikenya.com/portal/add_stock/
@login_required(login_url="accounts:signup")
def add_stock(request):

    categories_table = StockCategories.objects.all()

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
            messages.info(request, "Stock item saved successfully", extra_tags="success")
            # messages.error(request, 'Please verify your account from the link that was sent to your email.')

    return render(request, 'portal/add_stock.html', {"CategoriesTable": categories_table})


# mintarikenya.com/portal/manage_stock/
@login_required(login_url="accounts:signup")
def manage_stock(request):
    stock_table = Stock.objects.all()
    return render(request, 'portal/manage_stock.html', {"StockTable": stock_table})


# mintarikenya.com/portal/record_order/
@login_required(login_url="accounts:signup")
def record_order(request):
    stock_table = Stock.objects.all()

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
            messages.info(request, "Order recorded successfully", extra_tags="success")

    return render(request, 'portal/record_order.html', {"StockTable": stock_table})


# mintarikenya.com/portal/manage_orders/
@login_required(login_url="accounts:signup")
def manage_orders(request):
    records_table = RecordOrder.objects.all()

    # print(RecordsTable[0].LastName)

    return render(request, "portal/manage_orders.html", {"RecordsTable": records_table})


