from django.utils import timezone

from django.db import models
from django.urls import reverse

def one_week_hence():
    return timezone.now() +timezone.timedelta(days=7)


class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    