from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# mintarikenya.com
def index(request):
	return render(request, 'landing/global_index.html')