from django.urls import path


from . import views

urlpatterns = [
    path('create_todo/' , views.create_todo_view, name='create_todo'),
    path('todo_list' , views.todo_list_view, name ='todo_list'),
]