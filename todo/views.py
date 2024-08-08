from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm



# Create your views here.
def Index(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(Index)
    else:
        form = TaskForm()

    tasks_notcompleted = Task.objects.filter(is_done=False).order_by("priority")
    tasks_completed = Task.objects.filter(is_done=True).order_by("priority")
    context = {
        'tasks_notcompleted': tasks_notcompleted,
        'tasks_completed': tasks_completed,
        'form': form,
    }
    return render(request, 'index.html', context)


def Done(request, id):
    task = Task.objects.get(id=id)
    task.is_done = True
    task.save()
    return redirect(Index)

def Delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect(Index)
