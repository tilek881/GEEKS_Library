from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import TodoModel
from .forms import TodoForm

class TodoCreateView(CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo/create_todo.html'
    success_url = reverse_lazy('todo_list')

class TodoListView(ListView):
    model = TodoModel
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_list'
    ordering = ['-id']

class TodoDetailView(DetailView):
    model = TodoModel
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo'

class TodoDeleteView(DeleteView):
    model = TodoModel
    template_name = 'todo/delete_todo.html'
    success_url = reverse_lazy('todo_list')

