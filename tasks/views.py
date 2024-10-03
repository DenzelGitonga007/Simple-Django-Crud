from django.shortcuts import render, redirect
from . models import Task
from . forms import TaskCreateForm

# Create your views here.
# Create Task
def create_task(request):
    """ Create task """
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'tasks/create_task.html', context)

# Read all tasks
def task_list(request):
    """ View all tasks """
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/task_list.html', context)

# Edit task
def update_task(request, pk):
    """ Update/edit task """
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskCreateForm(instance=task)
    context = {
        'form': form
    }
    return render(request, 'tasks/update_task.html', context)

# Delete task
def delete_task(request, pk):
    """ Delete task """
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    context = {
        'task': task
    }
    return render(request, 'tasks/confirm_delete.html', context)

