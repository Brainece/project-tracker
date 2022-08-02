from django.db import models
from django.contrib.auth.models import User

# Create your models here.

status = (
    ('1', 'Stalled'),
    ('2', 'Ongoing'),
    ('3', 'Completed')
    )

class Project(models.Model):
    """A project that is should or is being worked on"""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    creation_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=7, choices=status, default=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=80)
    status = models.CharField(max_length=7, choices=status, default=2)

    class Meta:
        ordering = ['project', 'task_name']

    def __str__(self):
        return self.task_name
