from typing import Any
from django.db import models

# Create your models here.


class CommonAttributes(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(CommonAttributes):
    name = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Designation(CommonAttributes):
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    description = models.TextField(max_length=500)


class Employee(CommonAttributes):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=15, unique=True)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
