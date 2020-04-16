from django.db import models
from backend.utils import get_this_time_tomorrow
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.
class TodoItem(models.Model):
    class Priority(models.IntegerChoices):
        NORMAL = 0
        PRIORITY = 1
        URGENT = 2
        CRITICAL = 3

    class Meta:
        # order by updated in reverse order (most recent first)
        ordering = ['-updated']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(default=get_this_time_tomorrow)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True, default='')
    priority = models.IntegerField(choices=Priority.choices, default=0)
    owner = models.ForeignKey(get_user_model(), related_name='todoitems', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(TodoItem, self).save(*args, **kwargs)


class Note(models.Model):
    class Meta:
        ordering = ['-updated']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False, default='')
    owner = models.ForeignKey(get_user_model(), related_name='notes', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Note, self).save(*args, **kwargs)
