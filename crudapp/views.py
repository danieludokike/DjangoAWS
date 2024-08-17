from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Task


def get_tasks(user, task_id=None):
    if task_id is None:
        return Task.objects.filter(user=user)
    return Task.objects.get(id=task_id)


@login_required(login_url="auth:login")
def home_view(request):
    context = {"tasks": get_tasks(request.user) }
    return render(request, "crudapp/account.html", context)


@login_required(login_url="auth:login")
def add_task_view(request):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            task = Task(name=task, user=request.user)
            task.save()
            return redirect("crud:home")
        messages.error(request, "Please enter a task you want to add")
        return redirect("crud:home")
    return redirect("crud:home")


@login_required(login_url="auth:login")
def update_task_view(request, task_id):
    if request.method == "POST":
        task = request.POST.get("task")
        if task:
            current_task = get_tasks(request.user, task_id)
            current_task.name=task
            current_task.save()
            
            messages.error(request, "Updated successfully")
            return redirect("crud:home")
        
        messages.error(request, "We were unable to update your task")
        return redirect("crud:home")
    
    context = {"task": get_tasks(request.user, task_id)}
    return render(request, "crudapp/update.html", context)