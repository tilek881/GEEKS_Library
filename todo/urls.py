from django.urls import path
from . import views

urlpatterns = [
    path('create_todo/', views.TodoCreateView.as_view(), name='create_todo'),
    path('todo_detail/<int:pk>/', views.TodoDetailView.as_view(), name='todo_detail'),
    path('todo_list/', views.TodoListView.as_view(), name='todo_list'),
    path('todo/<int:pk>/delete/', views.TodoDeleteView.as_view(), name='delete_todo')
]
