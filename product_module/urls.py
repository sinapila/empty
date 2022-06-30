from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-categorys-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-brand-list'),
    # path('cat/<cat>/<brand>', views.ProductListView.as_view(), name='product-categorys-list'),
    # path('', views.product_list, name='product-list'),
    path('product-favarite', views.AddProductFavorite.as_view(), name='product-favarite'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
]
