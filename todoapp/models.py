from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_title= models. CharField(max_length=200)
    is_completed = models. BooleanField(default=False)
    todo_desc = models. TextField()
    created_at = models. DateTimeField(auto_now_add=True)
    updated_at = models. DateTimeField(auto_now=True)
    