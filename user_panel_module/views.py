from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class UserPanelDushbordPage(TemplateView):
    template_name = 'user_panel_module/user_panel_dashbord_page.html'