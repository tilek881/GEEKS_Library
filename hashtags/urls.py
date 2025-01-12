from django.urls import path
from . import views


urlpatterns = [
    path('fairy_tales/' , views.fairy_tales, name='fairy_tails'),
    path('fantasy/' , views.fantasy, name='fantasy'),
    path('drama/' , views.drama, name='drama'),

]