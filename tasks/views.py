from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')  # return to the same url

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):

    task = Task.objects.get(id=pk)  # retrieve an object

    # new item, field in a form already filled in
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        # the same instance, resend new data
        if form.is_valid():
            form.save()
        return redirect('/')  # return to the homepage

    context = {'form': form}  # pass it to the context attribute - publish

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):

    item_del = Task.objects.get(id=pk)

    if request.method == 'POST':
        item_del.delete()

        return redirect('/')  # return to the homepage

    context = {'item_del': item_del}

    return render(request, 'tasks/delete.html', context)
