from django.db import models


class Task(models.Model):
    class Priority(models.IntegerChoices):
        VERY_HIGH = 1, "خیلی مهم"
        HIGH = 2, "مهم"
        MEDIUM = 3, "متوسط"
        LOW = 4, "کم"
        VERY_LOW = 5, "خیلی کم"

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    priority = models.IntegerField(choices=Priority)
    is_done = models.BooleanField(default=False)

