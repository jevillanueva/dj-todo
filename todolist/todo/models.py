from django.db import models

# Create your models here.
class Task(models.Model): 
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_view_tasks", "Can view tasks"),
        ]