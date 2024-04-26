from typing import Any
from django.db import models

from base.constants import GENDER_CHOICES,  GENDER_OTHERS


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
    name = models.CharField(max_length=30, default='Developer', unique=True)
    description = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Employee(CommonAttributes):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=GENDER_OTHERS)
    email = models.EmailField(max_length=100, unique=True)
    contact = models.CharField(max_length=15, unique=True)
    password = models.TextField()
    designation = models.ForeignKey(
        Designation, on_delete=models.PROTECT, related_name='employee')
    photo = models.FileField(upload_to="employee/", null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class AddressInformation(CommonAttributes):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField()
    address_line_1 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self) -> str:
        return self.employee.first_name


class Documents(CommonAttributes):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name='documents')
    # TODO: Add choice fields
    type = models.CharField(max_length=6)
    file = models.FileField()
