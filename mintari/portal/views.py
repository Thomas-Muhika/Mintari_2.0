from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Sum
from django.views import View
from django.contrib.auth.models import User
from portal.models import RecordOrder, StockCategories, Stock, Order, BlogArticle
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


class EditStock(LoginRequiredMixin, View):
    login_url = "accounts:signin"

    def post(self, request, product_code):
        categories_table = StockCategories.objects.all()

        try:
            if request.POST.get('submit') == 'EditStock':
                stock_unit = Stock.objects.all().filter(ProductCode=product_code)[0]
                stock_unit.ProductTitle = request.POST['ProductTitle']
                stock_unit.ProductWeight = request.POST['ProductWeight']
                stock_unit.ProductDimension = request.POST['ProductDimension']
                stock_unit.ProductPrice = request.POST['BasePrice']
                stock_unit.DetailedDescription = request.POST['DetailedDescription']
                stock_unit.save()

                stock_table = Stock.objects.all()
                messages.success(request, "Stock updated successfully")
                return render(request, 'portal/manage_stock.html', {"StockTable": stock_table})
        except:
            messages.error(request, "Stock update failed, try again or contact the system administrator")
            stock_unit = Stock.objects.all().filter(ProductCode=product_code)[0]
            return render(request, 'portal/edit_stock.html',{"CategoriesTable": categories_table, "stock_unit": stock_unit})

    def get(self, request, product_code):
        categories_table = StockCategories.objects.all()
        stock_unit = Stock.objects.all().filter(ProductCode=product_code)[0]

        return render(request, 'portal/edit_stock.html', {"CategoriesTable": categories_table, "stock_unit": stock_unit})


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

# mintarikenya.com/portal/add_article/  ... blog article add
@login_required(login_url="accounts:signin")
def add_article(request):

    if request.method == 'POST':
        if request.POST.get('submit') == 'AddArticle':

            BlogArticle.objects.create(
                BlogMainImage=request.FILES['MainArticleImage'],
                ArticleTitle=request.POST['ArticleTitle'],
                ArticlePreface=request.POST['ArticlePreface'],
                SupportiveImage=request.FILES['SupportImage'],
                ArticleBody=request.POST['ArticleBody'],
                ArticleSubTitle=request.POST['ArticleSubTitle'],
                ArticleContinuation=request.POST['SubBody'],
                AdjournmentImage=request.FILES['AdjImage'],
                AdjournmentBody=request.POST['AdjournmentBody'],
                ArticleTag=request.POST['ArticleTag'],
                ArticleArtist=request.POST['Artist'],
            )
            messages.info(request, "Article saved successfully", extra_tags="success")
            # messages.error(request, 'Please verify your account from the link that was sent to your email.')

    return render(request, 'portal/add_article.html')

