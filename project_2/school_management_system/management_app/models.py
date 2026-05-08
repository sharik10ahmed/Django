from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    is_active_student = models.BooleanField(default=True)

    full_name = models.CharField(max_length=200)

    def __str__(self):
        return self.username