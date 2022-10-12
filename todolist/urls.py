# TODO: Implement Routings Here

from django.urls import path
from todolist.views import show_todolist

from todolist.views import register #sesuaikan dengan nama fungsi yang dibuat

from todolist.views import login_user #sesuaikan dengan nama fungsi yang dibuat

from todolist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat

from todolist.views import add_task, show_json, add_todolist #sesuaikan dengan nama fungsi yang dibuat

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task'),
    path('json/',show_json,name="show_json"),
    path('json/',show_json,name="show_json"),
    path('add/', add_todolist, name='add_todolist'),
]