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

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task = Task.objects.all().filter(user = request.user)

    context = {
        'username' : request.user,
        'list_task' : data_task
    }

    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
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
    item = Task.objects.get(pk = id)
    item.is_finished = item.is_finished ^ 1
    item.save()
    return HttpResponseRedirect('../')

def delete_task(request, id):
    item = Task.objects.get(pk = id)
    item.delete()
    return HttpResponseRedirect('../')
