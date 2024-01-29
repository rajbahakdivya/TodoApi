from django.db import models

class Task(models.Model):

    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
