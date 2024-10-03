from django import forms
from .models import Task

# Form to create the task
class TaskCreateForm(forms.ModelForm):
    """ Form to create a task """
    model = Task
    fields = ['title', 'description', 'status']