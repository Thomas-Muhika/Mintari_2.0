from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.views import View
from django.contrib.auth.models import User
from portal.models import RecordOrder, StockCategories, Stock, Order
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com/portal/
@login_required(login_url="accounts:signin")
def portal_index(request):

    try:
        total_deposit = RecordOrder.objects.aggregate(Sum('DepositPaid'))['DepositPaid__sum']
        total_deposit = 'Ksh {:,.2f}'.format(total_deposit)
    except:
        total_deposit = 0
        pass

    products_sold = len(RecordOrder.objects.all())

    return render(request, 'portal/dashboard.html', {'revenue': total_deposit, 'products_sold': products_sold})


@login_required(login_url="accounts:signin")
def calender(request):
    return render(request, 'portal/calender.html')


@login_required(login_url="accounts:signin")
def manage_categories(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'AddCategory':

            StockCategories.objects.create(
                category=request.POST['CategoryName'],
            )

    categories_table = StockCategories.objects.all()

    return render(request, 'portal/manage_categories.html', {"CategoriesTable": categories_table})


# mintarikenya.com/portal/add_stock/
@login_required(login_url="accounts:signin")
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
                DetailedDescription=request.POST['DetailedDescription'],
                ProductBaseImage=request.FILES['MainImage'],
                ProductImageTopView=request.FILES['ProductImageTopView'],
                ProductImageLeftView=request.FILES['ProductImageLeftView'],
                ProductImageFrontView=request.FILES['ProductImageFrontView'],
            )
            messages.info(request, "Stock item saved successfully", extra_tags="success")
            # messages.error(request, 'Please verify your account from the link that was sent to your email.')

    return render(request, 'portal/add_stock.html', {"CategoriesTable": categories_table})


# mintarikenya.com/portal/manage_stock/
@login_required(login_url="accounts:signin")
def manage_stock(request):
    stock_table = Stock.objects.all()
    return render(request, 'portal/manage_stock.html', {"StockTable": stock_table})


class DeleteStock(LoginRequiredMixin, View):
    login_url = "accounts:signin"

    def get(self, request, product_code):
        stock_unit = Stock.objects.get(ProductCode=product_code)
        stock_unit.delete()
        return redirect('portal:manage_stock')


# mintarikenya.com/portal/record_order/
@login_required(login_url="accounts:signin")
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
@login_required(login_url="accounts:signin")
def manage_orders(request):
    records_table = Order.objects.all()

    # print(RecordsTable[0].LastName)

    return render(request, "portal/manage_orders.html", {"RecordsTable": records_table})


class DeleteOrder(LoginRequiredMixin, View):
    login_url = "accounts:signin"

    def get(self, request, order_num):
        order_unit = Order.objects.get(OrderNumber=order_num)
        order_unit.delete()
        return redirect('portal:manage_orders')


@login_required(login_url="accounts:signin")
def users_tracking(request):
    users_table = User.objects.all()
    return render(request, 'portal/users_tracking.html', {"users_table": users_table})



