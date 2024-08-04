from django.shortcuts import render
from .models import Task


# Create your views here.
def Index(request):
    tasks_notcompleted = Task.objects.filter(is_done=False).order_by("priority")
    tasks_completed = Task.objects.filter(is_done=True).order_by("priority")
    context = {
        'tasks_notcompleted': tasks_notcompleted,
        'tasks_completed': tasks_completed,
    }
    return render(request, 'index.html', context)
