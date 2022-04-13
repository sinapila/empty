from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView

from site_module.models import SiteSetting
from .forms import ContactUsModelForm
# Create your views here.
from .models import UserProfile


class ContactUsView(CreateView):
    template_name = 'contact-module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, **kwargs):
        contaxt = super(ContactUsView, self).get_context_data()
        settings: SiteSetting = SiteSetting.objects.filter(is_main_settings=True).first()
        contaxt['settings'] = settings

        return contaxt



class CreateProfileViwe(CreateView):
    template_name = 'contact-module/create_profile_page.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'

class ProfileView(ListView):
    model = UserProfile
    template_name = 'contact-module/profiles_list.html'
    context_object_name = 'profiles'

