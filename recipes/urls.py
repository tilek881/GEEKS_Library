from django.urls import path
from .views import recipe_list, recipe_detail, add_recipe, add_ingredient, delete_recipe

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('<int:pk>/', recipe_detail, name='recipe_detail'),
    path('add/', add_recipe, name='add_recipe'),
    path('<int:pk>/add_ingredient/', add_ingredient, name='add_ingredient'),
    path('<int:pk>/delete/', delete_recipe, name='delete_recipe'),
]
