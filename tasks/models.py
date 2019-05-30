from django.db import models
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)


class Order(models.Model):
    task = models.OneToOneField(Task, on_delete=models.SET_NULL, null=True)
    open = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} + {} + {}'.format(self.open, self.task)

    def save(self, *args, **kwargs):
        _creating = False
        if not self.id:
            _creating = True
        super().save(*args, **kwargs)

        if _creating:
            self.task.done = False
            self.task.save()

        if not self.open:
            self.task.done = True
            self.task.save()


