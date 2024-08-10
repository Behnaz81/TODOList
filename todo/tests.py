from django.test import TestCase
from .models import Task
from .forms import TaskForm


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


class TaskFormTest(TestCase):
    def test_valid_form(self):
        form_date = {
            'title': 'Wash the dishes',
            'priority': 1,
            'description': 'There are too many'
        }
        form = TaskForm(data=form_date)

        self.assertTrue(form.is_valid())

        task = form.save()

        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.title, 'Wash the dishes')
        self.assertEqual(task.priority, 1)
        self.assertEqual(task.description, 'There are too many')
        self.assertEqual(task.is_done, False)

    def test_invalid_form(self):
        form_date = {
            'title': '',
            'priority': 1,
            'description': 'There are too many dishes'
        }

        form = TaskForm(data=form_date)

        self.assertFalse(form.is_valid())

        self.assertIn('title', form.errors)
        self.assertEqual(form.errors['title'], ['This field is required.'])

    def test_invalid_form2(self):
        form_data = {
            'title': 'Wash the dishes',
            'priority': '',
            'description': 'There are too many dishes'
        }

        form = TaskForm(data=form_data)

        self.assertFalse(form.is_valid())

        self.assertIn('priority', form.errors)
        self.assertEqual(form.errors['priority'], ['This field is required.'])

    def test_valid_form2(self):
        form_date = {
            'title': 'Wash the dishes',
            'priority': 1
        }

        form = TaskForm(data=form_date)

        self.assertTrue(form.is_valid())

        task = form.save()

        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.title, 'Wash the dishes')
        self.assertEqual(task.priority, 1)
        self.assertIsNone(task.description)
        self.assertEqual(task.is_done, False)
