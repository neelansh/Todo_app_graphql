from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length = 100)
    task_desc = models.CharField(max_length = 1000)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_name
