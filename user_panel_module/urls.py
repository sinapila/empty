from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserPanelDushbordPage.as_view(), 'user_panel_dashbord')
]
