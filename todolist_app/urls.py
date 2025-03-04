from django.contrib import admin
from django.urls import path, include
from todolist_app import views
#wpisując ręcznie w przeglądarce te Path, odwołamy sie do tych podstron

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('delete/<task_id>',views.delete_task, name='delete_task'),
    path('edit/<task_id>',views.edit_task, name='edit_task'),
    path('complete/<task_id>',views.complete_task, name='complete_task'),
    path('pending/<task_id>',views.pending_task, name='pending_task'),
]