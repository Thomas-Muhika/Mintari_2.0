from django.shortcuts import render

# Create your views here.
# /blog/
def index(request):
	return render(request, 'blog/index.html')


# /blog/blog-details/
def blog_details(request):
	return render(request, 'blog/blog-details.html')