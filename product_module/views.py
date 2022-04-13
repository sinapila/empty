from django.views import View
from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView,DetailView

from .models import Product


# Create your views here.

class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = [
        # '-price'
    ]
    paginate_by = 6



class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data()

        loaded_product = self.object
        request = self.request
        favarite_product_id = request.session.get('product_favarite')
        context['is_favorite'] = favarite_product_id == str(loaded_product.id)

        return context


class AddProductFavorite(View):
    def post(self,request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk = product_id)
        request.session['product_favarite'] = product_id
        return redirect(product.get_absolute_url())