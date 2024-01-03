from django.shortcuts import render
from task import models
from task import forms

def show_task(request):
    task = models.task_model.objects.all()
    return render(request, 'show.html', {'task':task})