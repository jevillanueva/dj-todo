from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('<int:task_id>/delete/', views.delete, name='delete'),
    path('<int:task_id>/edit/', views.edit, name='edit'),
    path('<int:task_id>/done/', views.done, name='done'),
    path('<int:task_id>/undone/', views.undone, name='undone'),
]
