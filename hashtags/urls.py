from django.urls import path
from . import views


urlpatterns = [
    path('all_product/' , views.all_products, name='all_products'),
    path('fairy_tale/', views.fairy_tale, name='fairy_tale'),
    path('fantasy/', views.fantasy, name='fantasy'),
    path('drama/', views.drama, name='drama'),

]