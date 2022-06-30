from django.contrib.auth import logout
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from .forms import EditUserForm, ChangePasswordForm


# Create your views here.

class UserDashbordPanel(TemplateView):
    template_name = 'user_module/user_dashbord.html'


class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        now_user = User.objects.filter(id=request.user.id).first()
        edit_user_form = EditUserForm(instance=now_user)
        return render(request, 'user_module/edit_profile_page.html', {
            'form': edit_user_form,
            'now': now_user
        })

    def post(self, request: HttpRequest):
        now_user = User.objects.filter(id=request.user.id).first()
        edit_form = EditUserForm(request.POST, request.FILES, instance=now_user)
        return render(request, 'user_module/edit_profile_page.html', {
            'form': edit_form,
            'now': now_user
        })


class ChangePassworldPage(View):
    def get(self, request: HttpRequest):
        form = ChangePasswordForm()
        return render(request, 'user_module/change_passworld_page.html', {'form': form})

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        now_user: User = User.objects.filter(id=request.user.id).first()

        if form.is_valid():
            if form.cleaned_data.get('password') == form.cleaned_data.get('confirm_password'):
                if now_user.check_password(form.cleaned_data.get('password')):
                    now_user.set_password(form.cleaned_data.get('password'))
                    now_user.save()
                    logout(request)
                    return redirect(reverse('login page'))
                else:
                    form.add_error('password','کلمه عبور وارد شده اشتباه میباشد')

        else:
            form.add_error('password', 'خطایی ناشناخته روی داد')



def user_panel_menu_component(request: HttpRequest):
    return render(request=request, template_name='user_module/components/user_panel_menu_component.html')

