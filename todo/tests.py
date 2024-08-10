from django.test import TestCase
from .models import Task


# Create your tests here.
class TaskModelTest(TestCase):
    def setUp(self):
        Task.objects.create(title="Wash the dishes", priority=1, description="There are too many dishes!")

    def test_task_title(self):
        task = Task.objects.get(title="Wash the dishes")
        self.assertEqual(task.title, "Wash the dishes")

    def test_task_priority(self):
        task = Task.objects.get(title="Wash the dishes")
        self.assertEqual(task.priority, 1)

    def test_task_description(self):
        task = Task.objects.get(title="Wash the dishes")
        self.assertEqual(task.description, "There are too many dishes!")