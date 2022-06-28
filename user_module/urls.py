from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserDashbordPanel.as_view(), name='user_dashbord'),
    path('/EditPage', views.EditUserProfilePage.as_view(), name='edit_profile_page'),
    path('/ChangePass', views.ChangePassworldPage.as_view(), name='change_passworld_page')
]
