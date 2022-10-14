from django.urls import path
from todolist.views import show_todolist
from todolist.views import show_todolist_json
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import change_status
from todolist.views import delete_task
from todolist.views import add 

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('change_status/<int:id>', change_status, name='change_status'),
    path('delete_task/<int:id>/', delete_task, name = 'delete_task'),
    path('add/', add, name = 'add'),
]