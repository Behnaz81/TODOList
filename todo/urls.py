from django.urls import path
from .views import TaskListView
from .views import TaskDeleteView
from .views import TaskUpdateView


urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('done/<int:pk>/', TaskUpdateView.as_view(), name='done'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
    path('edit/<int:task_id>/', TaskListView.as_view(), name='edit')
]
