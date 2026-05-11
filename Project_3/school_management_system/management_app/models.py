from django.db import models

# Create your models here.

# models.py

from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    # Dates
    date_added = models.DateTimeField(auto_now_add=True)
    date_of_birth = models.DateField()

    # Image
    image = models.ImageField(upload_to='students/', blank=True, null=True)

    # Address
    address = models.TextField()

    def __str__(self):
        return self.name