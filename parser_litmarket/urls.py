from django.urls import path
from . import views

urlpatterns = [
    path('litmarket_list', views.LitmarketListView.as_view(), name='litmarket_list'),
    path('litmarket_form' , views.LitmarketFormView.as_view(), name='litmarket_form'),
]