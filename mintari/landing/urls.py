from django.urls import path, re_path

from . import views

app_name = 'landing'

urlpatterns = [
    # mintarikenya.co.ke
    re_path(r'^$', views.index, name='index'),

    # mintarikenya.co.ke/contact&us/
    re_path(r'^contact&us/$', views.contact__us, name='contact_us'),

    # mintarikenya.co.ke/aboutUs/
    re_path(r'^aboutUs/$', views.about_us, name='aboutUs'),

    # mintarikenya.co.ke/coming_soon/
    re_path(r'^coming_soon/$', views.coming_soon, name='coming_soon'),
]