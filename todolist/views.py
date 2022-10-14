from operator import is_
from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TaskForm
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseBadRequest, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.all().filter(user=request.user)

    context = {
        'username': request.user,
        'list_task': data_task
    }

    return render(request, "todolist.html", context)


@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    data_task = Task.objects.all().filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data_task), content_type="application/json")


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response


def create_task(request):

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.user = request.user
            model_instance.date = datetime.date.today()
            model_instance.title = request.POST.get('title')
            model_instance.description = request.POST.get('description')
            model_instance.save()
            return HttpResponseRedirect('../')
    context = {
        'form': form
    }

    return render(request, 'create_task.html', context)


def change_status(request, id):
    item = Task.objects.get(pk=id)
    item.is_finished = item.is_finished ^ 1

    if (item.is_finished == True):
        item.status = 'Selesai'
    else:
        item.status = 'Belum Selesai'

    item.save()
    return HttpResponseRedirect('../')

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_task(request, id):
    item = Task.objects.get(pk=id)
    item.delete()
    return redirect('todolist:show_todolist')


@login_required(login_url='/todolist/login/')
@csrf_exempt
def add(request):
    if request.method == 'POST':
        
        user = request.user
        date = datetime.date.today()
        title = request.POST.get("title")
        description = request.POST.get("description")
        is_finished = False
        status = "Belum selesai"
        
        new_task = Task(user=user, date=date, title=title, description=description, 
                        is_finished=is_finished, status=status)
        new_task.save()

        return JsonResponse({

            "pk": new_task.pk,
            "fields":
            {
                "user": new_task.user.username,
                "date": new_task.date,
                "title": new_task.title,
                "description": new_task.description,
                "is_finished": new_task.is_finished,
                "status": new_task.status,
            }
        })
    else:
        return HttpResponseBadRequest('Invalid request')
