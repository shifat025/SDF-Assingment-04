from django.shortcuts import render,redirect
from . import models
from . import forms


# Create your views here.


def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
            
        
    else:
        task_form=forms.TaskForm()
    return render(request,'task.html', {'form':task_form})

def edit(request, id):
    task_id = models.task_model.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task_id)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task_id)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')
            
    return render(request,'task.html', {'form':task_form})

def delete(request, id):
    task_id = models.task_model.objects.get(pk=id)
    task_id.delete()
    return redirect('show_task')

def complete(request, id):
    task_id = models.task_model.objects.get(pk=id)
    task_id.is_completed = True
    task_id.save()
    return redirect('show_task')