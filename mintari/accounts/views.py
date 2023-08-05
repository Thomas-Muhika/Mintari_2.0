from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import UserCreationForm
from django.db import IntegrityError
from django.contrib import messages

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

                        # message = get_template('accounts/WelcomePlayer.html').render({"user_name": user.first_name})
                        # mail = EmailMessage('Welcome to MASAIMEGA Family', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
                        # mail.content_subtype = 'html'
                        # mail.send()

                    except IntegrityError:
                        messages.error(request, 'A user with that Phone Number is already registered. Try logging in.', extra_tags="error")
                        return render(request, 'portal/signup.html', {'form': form, 'ucf': ucf})

                    return redirect('landing:index')

                else:
                    messages.error(request, 'reCAPTCHA validation failed. Please reload page and try again.', extra_tags="error")
                    return render(request, 'portal/signup.html', {'form': form, 'ucf': ucf})

            else:
                messages.error(request, 'The password you entered is too simple and can easily be guessed, please try again with a different password.', extra_tags="error")

        return render(request, 'portal/signup.html', {'form': form, 'ucf': ucf})


# mintarikenya.co.ke/accounts/signin/
def sign_in(request):
    return render(request, 'portal/sign_up.html')


# mintarikenya.co.ke/accounts/forgot_password/
def forgot_password(request):
    return render(request, 'portal/forgot_password.html')
