from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com
def index(request):
	return render(request, 'landing/global_index.html')


def contact__us(request):
	return render(request, 'landing/contact_us.html')


def coming_soon(request):
	return render(request, 'landing/coming_soon.html')


def about_us(request):
	return render(request, 'landing/aboutUs.html')
