from django.shortcuts import render
from django.views import View

from portal.models import BlogArticle

# Create your views here.
# /blog/
def index(request):
	stock_table = BlogArticle.objects.all()

	context = {
		"blog_articles": BlogArticle.objects.all()[:3],
		"lifestyle_article_main": BlogArticle.objects.all().filter(ArticleTag='LifeStyle')[:1],
		"lifestyle_articles": BlogArticle.objects.all().filter(ArticleTag='LifeStyle')[:4],
		"artspace_articles_main": BlogArticle.objects.all().filter(ArticleTag='Art Space')[:1],
		"artspace_articles_left": BlogArticle.objects.all().filter(ArticleTag='Art Space')[:4],
		"artspace_articles_right": BlogArticle.objects.all().filter(ArticleTag='Art Space')[4:8],
		"upholstery_articles_main": BlogArticle.objects.all().filter(ArticleTag='upholstery')[:3],
		"upholstery_articles": BlogArticle.objects.all().filter(ArticleTag='upholstery')[:4],
		"latest_articles": BlogArticle.objects.all().order_by('-date_created')[:3],
		"popular_articles": BlogArticle.objects.all().order_by('date_created')[:4],
		"featured_article": BlogArticle.objects.all().filter(ArticleTag='featured')[:1],
	}

	return render(request, 'blog/index.html', context)

# /blog/<blog title>
class BlogDetails(View):
	def get(self, request, blog_title):

		context = {
			"blog_article": BlogArticle.objects.all().filter(ArticleTitle=blog_title)[:1]
		}
		return render(request, 'blog/blog-details.html', context)

# /blog/<blog category>
class BlogCategory(View):
	def get(self, request, blog_category):

		context = {
			"blog_category_articles": BlogArticle.objects.all().filter(ArticleTag=blog_category),
			"blog_category": blog_category,
		}
		return render(request, 'blog/blog-category.html', context)


# /blog/blog-details/
def blog_details(request):
	return render(request, 'blog/blog-details.html')