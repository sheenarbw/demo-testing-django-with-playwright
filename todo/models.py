from django.db import models
from django.utils import timezone


class TodoItem(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description

    def is_overdue(self):
        return self.due_date < timezone.now().date()


# tags, dayplan
