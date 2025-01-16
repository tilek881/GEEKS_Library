from django.shortcuts import render, redirect , get_object_or_404


from . import forms , models

def create_todo_view(request):
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = forms.TodoForm()
    return render(request, template_name='todo/create_todo.html', context={'form': form})


def todo_list_view(request):
    if request.method == 'GET':
        todo_list = models.TodoModel.objects.all().order_by("-id")
        context = {"todo_list": todo_list}
        return render(request, template_name='todo/todo_list.html', context=context)


def todo_detail_view(request , id):
    if request.method == 'GET':
        todo_id = get_object_or_404(models.TodoModel, id =id)
        context = {'todo_id':todo_id}
        return render(request,template_name='todo/todo_detail.html' , context=context)


