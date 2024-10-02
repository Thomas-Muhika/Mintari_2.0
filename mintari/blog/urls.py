from django.urls import path, re_path

from . import views

app_name = 'blog'

urlpatterns = [
    # /blog/
    re_path(r'^$', views.index, name='index'),

    # /blog/<blog title>
    path('<str:blog_title>/', views.BlogDetails.as_view(), name='article'),

    # /blog/blog-details/
    re_path(r'^blog-details/$', views.blog_details, name='blog-details'),
]