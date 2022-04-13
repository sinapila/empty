from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View

from utils.email_service import send_email
from .forms import RegisterForm, LoginForm, ForgetpassForm, ResetPasswordForm
from .models import User


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # todo: send email active code
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate_account.html')
                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }

        return render(request, 'account_module/register.html', context)


class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login_page'))
            else:
                # todo: show your account was activated message to user
                pass

        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }

        return render(request, 'account_module/login.html', context)


class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass = ForgetpassForm()
        return render(request, 'account_module/Forgot_passworld.html', {
            'forget_pass': forget_pass
        })

    def post(self, request: HttpRequest):
        forget_pass_form = ForgetpassForm(request.POST)

        if forget_pass_form.is_valid():
            user: User = User.objects.filter(
                email__iexact=forget_pass_form.cleaned_data.get('email')).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgat_password.html')
                return redirect(reverse('login_page'))

        return render(request, 'account_module/Forgot_passworld.html', {
            'forget_pass': forget_pass_form
        })


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):

        user: User = User.objects.filter(email_active_code__iexact=active_code).first()

        if user is not None:
            reset_pass_form = ResetPasswordForm()
            return render(request, 'account_module/reset_password.html', {
                'reset_pass_form': reset_pass_form,
                'user': user
            })
        else:
            return redirect(reverse('login_page'))

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)

        if reset_pass_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is not None:
                user.set_password(reset_pass_form.cleaned_data.get('password'))
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login_page'))
            else:
                reset_pass_form.add_error('password', 'خطایی رخ داد')

        else:
            reset_pass_form.add_error('password', 'درست نیست')

        return redirect(reverse('login_page'))


class LogOutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return  redirect(reverse('login_page'))
