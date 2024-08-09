from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'task_id' in self.kwargs:
            task = get_object_or_404(Task, pk=self.kwargs['task_id'])
            context['form'] = TaskForm(instance=task)
            context['editing'] = True
            context['task_id'] = task.id
        else:
            context['form'] = TaskForm()
            context['editing'] = False

        context['tasks_notcompleted'] = Task.objects.filter(is_done=False).order_by("priority")
        context['tasks_completed'] = Task.objects.filter(is_done=True).order_by("priority")

        return context

    def post(self, request, *args, **kwargs):
        if 'task_id' in self.kwargs:
            task = get_object_or_404(Task, pk=self.kwargs['task_id'])
            form = TaskForm(request.POST, instance=task)
        else:
            form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return self.get(request, *args, form=form, **kwargs)


class TaskDeleteView(View):
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.delete()
        return redirect(self.success_url)


class TaskUpdateView(View):
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=kwargs['pk'])
        task.is_done = True
        task.save()
        return redirect(self.success_url)
