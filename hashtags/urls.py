from django.urls import path
from .views import AllProductsView, FairyTaleView, FantasyView, DramaView

urlpatterns = [
    path('all_product/', AllProductsView.as_view(), name='all_products'),
    path('fairy_tale/', FairyTaleView.as_view(), name='fairy_tale'),
    path('fantasy/', FantasyView.as_view(), name='fantasy'),
    path('drama/', DramaView.as_view(), name='drama'),
]
