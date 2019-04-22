from django import forms

from task.models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(help_text="Please enter TASK name.")
    description = forms.CharField(help_text="description")

    class Meta:
        model = Task
        fields = ['name','description']