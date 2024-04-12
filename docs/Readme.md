# Simple Todo App with Django

First, you need to install Django. You can do this by running the following command:

```bash
pip install django
```

Create a new Django project with the following command:

```bash
django-admin startproject todolist
```

Then, you can create a new Django app with the following command:

```bash
python manage.py startapp todo
```

Create models for the app in the `models.py` file in the `todo` directory:

```python
from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    completed = models.BooleanField(default=False)
```

Create a migration for the models with the following command:

```bash
python manage.py makemigrations
python manage.py migrate
```

Enable content task in the admin panel

```python
from django.contrib import admin
from .models import Task

admin.site.register(Task)
```

Create get view index in the `views.py` file in the `todo` directory:

```python
from django.shortcuts import render
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})
```

Create a template for the view in the `templates/todo` directory:

```html
...
{% for task in tasks %}
    <li>{{ task.content }}</li>
{% endfor %}
...
```

Create a URL pattern for the view in the `urls.py` file in the `todo` directory:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Include the URL pattern in the main `urls.py` file in the `todolist` directory:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
```

Create a superuser with the following command:

```bash
python manage.py createsuperuser
```



Then, you can run the following command to start the server:

```bash
python manage.py runserver
```

