from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Task, status_choices


# Create your views here.


def index(request):
    tasks = Task.objects.order_by()
    return render(request, "index.html", context={"tasks": tasks})


def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {'status_choices': status_choices})
    else:
        Task.objects.create(
            description=request.POST.get("description"),
            status=request.POST.get("status"),
            date=request.POST.get("date")
        )
        return HttpResponseRedirect("/")


def task_detail(request):
    try:
        task = Task.objects.get(id=request.POST.get("id"))
    except Task.DoesNotExist:
        return HttpResponseRedirect("/")