from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('executor', 'Executor'),
    )
    user_type = models.CharField(max_length=120, choices=USER_TYPE_CHOICES, default='customer')
    balance = models.PositiveIntegerField(default=0)
