from django.urls import path, re_path

from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    re_path(r'^$', views.index, name='index'),

    # /blog/<blog title>
    path('<str:blog_title>/', views.BlogDetails.as_view(), name='article'),

    # /blog/category/<blog category>/
    path('category/<str:blog_category>/', views.BlogCategory.as_view(), name='blog_category'),

    # /blog/category/all/
    path('category/categories/all/', views.blog_categories, name='blog_categories'),

    # /blog/blog-details/
    re_path(r'^blog-details/$', views.blog_details, name='blog-details'),
]