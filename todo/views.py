from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse


# Create your views here.
def Index(request):
    tasks_notcompleted = Task.objects.filter(is_done=False).order_by("priority")
    tasks_completed = Task.objects.filter(is_done=True).order_by("priority")
    context = {
        'tasks_notcompleted': tasks_notcompleted,
        'tasks_completed': tasks_completed,
    }
    return render(request, 'index.html', context)


def Done(request, id):
    task = Task.objects.get(id=id)
    task.is_done = True
    task.save()
    return redirect(Index)
