from django.shortcuts import render, redirect, reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import IntegrityError
from django.contrib import messages
from django.conf import settings
import random
import string
import urllib
import json

from .forms import UserCreationForm


def sign_up(request):
    if request.user.is_authenticated:  # if user is already authenticated
        return redirect('landing:index')
    else:
        form = AuthenticationForm(data=request.POST)

        ucf = UserCreationForm(request.POST)  # user creation form

        if request.method == 'POST':
            if request.POST.get('submit') == 'sign_up':

                if ucf.is_valid():

                    # # reCAPTCHA validation
                    # ''' Begin reCAPTCHA validation '''
                    # recaptcha_response = request.POST.get('g-recaptcha-response')
                    # url = 'https://www.google.com/recaptcha/api/siteverify'
                    # values = {
                    #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    #     'response': recaptcha_response
                    # }
                    # data = urllib.parse.urlencode(values).encode("utf-8")
                    # req = urllib.request.Request(url, data)
                    # response = urllib.request.urlopen(req)
                    # result = json.load(response)  # *result* of reCAPTCHA validation
                    # ''' End reCAPTCHA validation '''

                    # if result['success']:
                    try:
                        # save auth from player creation form
                        user = ucf.save(commit=False)
                        user_phone = str(request.POST['phone_no'])
                        user.username = user_phone
                        user.is_active = True
                        user.save()

                        try:
                            message = get_template('accounts/welcome.html').render({"user_name": user.first_name})
                            mail = EmailMessage('Welcome to MINTARI Family', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
                            mail.content_subtype = 'html'
                            mail.send()

                            messages.success(request, 'Your account has been created, and an email has been sent to you, please sign in',
                                             extra_tags="error")
                            return redirect('accounts:signin')
                        except:
                            messages.success(request, 'Your account has been created, please sign in',
                                             extra_tags="error")
                            return redirect('accounts:signin')

                    except IntegrityError:
                        messages.error(request, 'A user with that Phone Number is already registered. Try logging in.', extra_tags="error")
                        return render(request, 'portal/signup.html', {'form': form, 'ucf': ucf})

                else:
                    messages.error(request,
                                   'The password you entered is too simple and can easily be guessed, please try again with a different password.',
                                   extra_tags="error")
                    # messages.error(request, 'reCAPTCHA validation failed. Please reload page and try again.', extra_tags="error")
                    return render(request, 'portal/signup.html', {'form': form, 'ucf': ucf})

            else:
                messages.error(request, 'The password you entered is too simple and can easily be guessed, please try again with a different password.', extra_tags="error")

        return render(request, 'portal/signup.html', {'form': form, 'ucf': ucf})


# mintarikenya.co.ke/accounts/signin/
def sign_in(request):
    if request.user.is_authenticated:  # if user is already authenticated
        return redirect('landing:index')
    else:
        form = AuthenticationForm(data=request.POST)

        if request.method == 'POST':
            if request.POST.get('submit') == 'log_in':

                # # reCAPTCHA validation
                # ''' Begin reCAPTCHA validation '''
                # recaptcha_response = request.POST.get('g-recaptcha-response')
                # url = 'https://www.google.com/recaptcha/api/siteverify'
                # values = {
                #     'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                #     'response': recaptcha_response
                # }
                # data = urllib.parse.urlencode(values).encode("utf-8")
                # req = urllib.request.Request(url, data)
                # response = urllib.request.urlopen(req)
                # result = json.load(response)  # *result* of reCAPTCHA validation
                # ''' End reCAPTCHA validation '''

                # if result['success']:
                username = str(request.POST['phone_number'])
                password = request.POST['password']

                user = authenticate(request, username=username, password=password)

                if user is not None:
                    if user.is_active:
                        if user.is_staff:
                            login(request, user)
                            return redirect('portal:portal_index')
                        else:
                            login(request, user)
                            return redirect('landing:index')
                    else:
                        # if user not active
                        messages.error(request, 'Please verify your account from the link that was sent to your email.', extra_tags="error")
                else:
                    # if user not active (email and password)
                    messages.error(request, 'There is no account with those details exists, please verify your login details or create an account.', extra_tags="error")
            else:
                # if recapture != success
                messages.error(request, 'reCAPTCHA validation failed. Please reload page and try again.', extra_tags="error")
        return render(request, 'portal/signin.html', {'form': form})


# mintarikenya.co.ke/accounts/forgot_password/
def forgot_password(request):
    return render(request, 'portal/forgot_password.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landing:index')
    else:
        logout(request)
        return redirect('landing:index')


def reset_password(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'ResetPassword':
            user_email = request.POST['email']
            user_objs = User.objects.all().filter(email=user_email)

            hidden_tag = 'hidden'

            if len(user_objs) > 0:
                # user exists

                def randomString(stringLength):
                    letters = string.ascii_letters
                    return ''.join(random.choice(letters) for i in range(stringLength))

                random_password = randomString(8)

                # change user password to a random password
                this_user = User.objects.get(email=user_email)
                this_user_fullnames = str(this_user.first_name) + ' ' + str(this_user.last_name)
                this_user.password = random_password
                this_user.save()

                message = get_template('accounts/ResetPassword.html').render({"this_user_fullnames": this_user_fullnames, "random_password": random_password})
                mail = EmailMessage('MASAIMEGA | Password Reset', message, to=[user_email], from_email=settings.EMAIL_HOST_USER)
                mail.content_subtype = 'html'
                mail.send()

                messages.success(request, 'An Email has been sent to you. Details of the requested password reset are in the email.', extra_tags="success")
                return render(request, 'landing/lost_password.html', {"hidden_tag": hidden_tag})
            else:
                # user does not exist
                messages.error(request, 'There is no account linked to that email address. Create an account by following the link *SignUp* beside.', extra_tags="warning")
                return render(request, 'landing/lost_password.html', {"hidden_tag": hidden_tag})

    return render(request, 'landing/lost_password.html')
