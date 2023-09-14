from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

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


def contact_us(request):
	if request.method == 'POST':
		if request.POST.get('submit') == 'contact_form':
			try:
				message = request.POST['your_message']
				name = request.POST['your_name']
				email = request.POST['your_email']

				# mail structure
				client_message = message + "\n\nclient name:  " + str(name) + "\nclient email:  " + str(email)

				# sending mail
				mail = EmailMessage('CONTACT FORM', client_message, to=['sales@mintarikenya.com'], from_email=settings.EMAIL_HOST_USER)
				mail.send()

				messages.info(request,'Your email has been sent successfully, we will look into it and provide you a response soon.',)
			except:
				messages.info(request,'There is a problem sending your information, kindly call us or try again.')

	return render(request, 'landing/contact_us.html')


def coming_soon(request):
	return render(request, 'landing/404.html')


def about_us(request):
	return render(request, 'landing/aboutUs.html')


# custom 404 view
def custom_404(request, exception):
	return render(request, 'landing/404.html', status=404)

