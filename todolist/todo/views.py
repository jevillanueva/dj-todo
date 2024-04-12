from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, "todo/index.html", {"tasks": tasks})


def detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, "todo/detail.html", {"task": task})


def new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:detail", task_id=task.id)
    else:
        form = TaskForm()
    return render(request, "todo/new.html", {"form": form, "task": None})


def edit(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect("tasks:detail", task_id=task.id)
    else:
        form = TaskForm(instance=task)
    return render(request, "todo/new.html", {"form": form, "task": task})


def delete(request, task_id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, pk=task_id)
        task.delete()
    return redirect("tasks:index")

def done(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = True
    task.save()
    return redirect("tasks:index")

def undone(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = False
    task.save()
    return redirect("tasks:index")