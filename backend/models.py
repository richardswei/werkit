from django.db import models
from backend.utils import get_this_time_tomorrow


# Create your models here.
class TodoItem(models.Model):
    class Priority(models.IntegerChoices):
        NORMAL = 0
        PRIORITY = 1
        URGENT = 2
        CRITICAL = 3

    class Meta:
        ordering = ['updated']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(default=get_this_time_tomorrow)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    priority = models.IntegerField(choices=Priority.choices, default=0)


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)

    class Meta:
        ordering = ['updated']
