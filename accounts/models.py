from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('executor', 'Executor'),
    )
    user_type = models.CharField(max_length=120, choices=USER_TYPE_CHOICES, default='customer')
