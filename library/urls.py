from django.urls import path
from . import views


urlpatterns = {
    path('library/', views.about_me, name='library'),
    path('about_my_pets/' , views.about_my_pets , name='about_my_pets'),
    path('date_time/' , views.date_time , name='date_time'),
}