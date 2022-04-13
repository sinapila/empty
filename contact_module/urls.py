from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactUsView.as_view(), name = 'contact_us_page'),
    path('create-profile/', views.CreateProfileViwe.as_view(), name='create_profile_page'),
    path('profile/', views.ProfileView.as_view(), name='create_profile_page'),
]
