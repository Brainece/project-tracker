from django import forms

from .models import Project, Task

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title']
       # labels = {'title': ''}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name']
        labels = {'text': 'Task: '}
        widgets = {'text': forms.Textarea(attrs={'cols':80})
            }
            

    