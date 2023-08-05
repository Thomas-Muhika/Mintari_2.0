from django.urls import path, re_path

from . import views

app_name = 'accounts'

urlpatterns = [
    # mintarikenya.co.ke/accounts/signup/
    re_path(r'^signup/$', views.sign_up, name='signup'),

    # mintarikenya.co.ke/accounts/signin/
    re_path(r'^signin/$', views.sign_in, name='signin'),

    # mintarikenya.co.ke/accounts/forgot_password/
    re_path(r'^forgot_password/$', views.forgot_password, name='forgot_password'),
]