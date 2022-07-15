from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic import ListView

from site_module.models import SiteBanner
from .models import Product
from .models import ProductCategory, ProductBrand


# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = [
        # '-price'
    ]
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 10000

        context['db_max_price'], context['start_price'], context['end_price'] = db_max_price, self.request.GET.get(
            "start_price") or 0, self.request.GET.get('end_price') or db_max_price

        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPositions.product_list)

        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()

        category = self.kwargs.get('cat')
        brand = self.kwargs.get('brand')
        start_price = self.request.GET.get('start_price')
        end_price = self.request.GET.get('end_price')

        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

        if category is not None:
            query = query.filter(category__url_title__iexact=category)

        if brand is not None:
            query = query.filter(brand__url_title__iexact=brand)

        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()

        loaded_product = self.object
        request = self.request
        favarite_product_id = request.session.get('product_favarite')
        context['is_favorite'] = favarite_product_id == str(loaded_product.id)
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPositions.product_detail)

        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_favarite'] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categorys = ProductCategory.objects.filter(is_active=True, is_delete=False)
    return render(request, 'product_module/components/product_categorys_components.html',
                  {'product_categorys': product_categorys,
                   'request': request})


def product_brand_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(product_count=Count('product')).filter(is_active=True)
    return render(request, 'product_module/components/product_brand_components.html',
                  {'product_brands': product_brands,
                   'request': request})
