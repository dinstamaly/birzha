from django.db import models
from django.utils import timezone

from accounts.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
    task = models.OneToOneField(Task, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    open = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'id:{} + user:{} + {} '.format(self.id, self.user, self.open)

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
            self.user.balance += self.task.price
            self.task.price = 0
            self.user.save()
            self.task.save()


