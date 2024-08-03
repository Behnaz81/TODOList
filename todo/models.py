from django.db import models


class Task(models.Model):
    class Priority(models.IntegerChoices):
        VERY_HIGH = 1
        HIGH = 2
        MEDIUM = 3
        LOW = 4
        VERY_LOW = 5

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    priority = models.IntegerField(choices=Priority)
    is_done = models.BooleanField(default=False)

