from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from portal.models import StockCategories, Stock


# mintarikenya.com
def index(request):
	stock_table = Stock.objects.all()

	context = {
		"sofa_items": Stock.objects.all().filter(ProductCategory='Sofas')[:2],
		"bed_items": Stock.objects.all().filter(ProductCategory='Beds')[:2],
		"dining_items": Stock.objects.all().filter(ProductCategory='Dining')[:2],
		"chair_items": Stock.objects.all().filter(ProductCategory='Chairs')[:1],
		"stools_items": Stock.objects.all().filter(ProductCategory='Stools')[:1],
		"accessories_items": Stock.objects.all().filter(ProductCategory='Accessories')[:1]
	}

	return render(request, 'landing/global_index.html', context)


def contact__us(request):
	return render(request, 'landing/contact_us.html')


def coming_soon(request):
	return render(request, 'landing/coming_soon.html')


def about_us(request):
	return render(request, 'landing/aboutUs.html')


# custom 404 view
def custom_404(request, exception):
	return render(request, 'landing/404.html', status=404)

