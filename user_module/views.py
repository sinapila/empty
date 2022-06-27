from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class UserDashbordPanel(TemplateView):
    template_name = 'templates/user_module/user_dashbord.html'