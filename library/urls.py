from django.urls import path
from . import views
from .views import BooksListView, BookDetailView

urlpatterns = [
    path('', views.BooksListView.as_view(), name='books_lists'),
    path('book_detail/<int:pk>/', views.BookDetailView.as_view(), name='books_detail'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pets/' , views.about_my_pets , name='about_my_pets'),
    path('date_time/' , views.date_time , name='date_time'),
    path('search/', views.SearchView.as_view(), name='search'),

]