from django.shortcuts import render, redirect
from tasks.forms import CreateTaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task


@login_required()
def create_task(request):
    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()

            return redirect("list_projects")

    else:
        form = CreateTaskForm()

    context = {
        "form": form,
    }
    return render(request, "create_task.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "show_my_tasks.html", context)
