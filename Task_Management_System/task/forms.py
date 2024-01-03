from django import forms
from .models import task_model

class TaskForm(forms.ModelForm):
    class Meta:
        model = task_model
        fields = '__all__'