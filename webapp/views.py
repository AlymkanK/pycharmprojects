from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Task, status_choices



# Create your views here.


def index(request):
    tasks = Task.objects.order_by('date')
    return render(request, "index.html", context={"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html",
                      context= {'task':get_object_or_404(Task, pk=1)}
                      )
    else:
        Task.objects.create(
            description=request.POST.get("description"),
            status=request.POST.get("status"),
            date=request.POST.get("date")
        )
        return HttpResponseRedirect(reverse("todolist"))


def task_detail(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_detail.html", context={"task": task})


def update_task(request, *args, pk, **kwargs):
    if request.method == "GET":
        return render(request, "update_task.html", {'status_choices': status_choices})
    else:
        Task.objects.create(
            description=request.POST.get("description"),
            status=request.POST.get("status"),
            date=request.POST.get("date")
        )
        return redirect('task_detail', pk=pk)


def delete_task(request, *args, pk, **kwargs):
    if request.method == "GET":
        task = get_object_or_404(Task, pk=pk)
        return render(request, "delete_task.html", context={"task": task})
    else:
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('tasks')