from django.shortcuts import render
from .models import Task


# Create your views here.
def Index(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)
