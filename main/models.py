from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
import environ

env = environ.Env()
environ.Env.read_env()

# Create your models here.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField(null=True)

    def __str__(self):
        return self.text