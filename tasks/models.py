from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)


