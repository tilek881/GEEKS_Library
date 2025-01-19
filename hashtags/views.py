from django.views.generic import ListView
from .models import Product


class AllProductsView(ListView):
    model = Product
    template_name = 'hashtags/all_products.html'
    context_object_name = 'products'


class FairyTaleView(ListView):
    model = Product
    template_name = 'hashtags/fairy_tale.html'
    context_object_name = 'fairy_tale'

    def get_queryset(self):
        return Product.objects.filter(tags__name='fairy tale')


class FantasyView(ListView):
    model = Product
    template_name = 'hashtags/fantasy.html'
    context_object_name = 'fantasy'

    def get_queryset(self):
        return Product.objects.filter(tags__name='fantasy')


class DramaView(ListView):
    model = Product
    template_name = 'hashtags/drama.html'
    context_object_name = 'drama'

    def get_queryset(self):
        return Product.objects.filter(tags__name='drama')
