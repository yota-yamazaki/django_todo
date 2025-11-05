from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoTask
from .forms import TodoTaskForm

# task listを表示する機能
def todo_list(request):
    tasks = TodoTask.objects.all()
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

def todo_create(request):
    if request.method == 'POST':
        form = TodoTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoTaskForm()

    return render(request, 'todo/todo_form.html', {'form': form})

# TODOを更新する機構
def todo_update(request, pk):
    task = get_object_or_404(TodoTask, pk=pk)
    if request.method == 'POST':
        form = TodoTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoTaskForm(instance=task)

    return render(request, 'todo/todo_form.html', {'form': form})

# Todoを削除する機能
def todo_delete(request, pk):
    task = get_object_or_404(TodoTask, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')

    return render(request, 'todo/todo_confirm_delete.html', {'task': task})

