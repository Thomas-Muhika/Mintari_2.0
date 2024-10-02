from django.shortcuts import render
from django.views import View

from portal.models import BlogArticle

# Create your views here.
# /blog/
def index(request):
	stock_table = BlogArticle.objects.all()

	context = {
		"blog_articles": BlogArticle.objects.all()[:3],
		"lifestyle_article_main": BlogArticle.objects.all().filter(ArticleTag='Lifestyle')[:1],
		"lifestyle_articles": BlogArticle.objects.all().filter(ArticleTag='Lifestyle')[:4],
		"upholstery_articles_main": BlogArticle.objects.all().filter(ArticleTag='upholstery')[:3],
		"upholstery_articles": BlogArticle.objects.all().filter(ArticleTag='upholstery')[:4],

	}

	return render(request, 'blog/index.html', context)

# /blog/<blog title>
class BlogDetails(View):
	def get(self, request, blog_title):

		context = {
			"blog_article": BlogArticle.objects.all().filter(ArticleTitle=blog_title)[:1]
		}
		return render(request, 'blog/blog-details.html', context)


# /blog/blog-details/
def blog_details(request):
	return render(request, 'blog/blog-details.html')