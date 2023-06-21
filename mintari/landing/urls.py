from django.urls import path, re_path

from . import views

app_name = 'landing'

urlpatterns = [
    # mintarikenya.com
    re_path(r'^$', views.index, name='index'),
]