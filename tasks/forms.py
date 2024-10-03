from django import forms
from .models import Task

# Form to create the task
class TaskCreateForm(forms.ModelForm):
    """Form to create a task"""
    class Meta:
        model = Task  # Link to the Task model
        fields = ['title', 'description', 'status']  # Specify the model fields to include in the form
