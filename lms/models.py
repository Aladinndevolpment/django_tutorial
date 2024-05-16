from django.db import models

# Create your models here.


class CommonAttributes(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Employee(CommonAttributes):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, db_index=True)
    password = models.TextField()
    dob = models.DateTimeField()

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Lead(CommonAttributes):
    name = models.CharField(max_length=50)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=15)
    employee = models.ForeignKey(
        Employee, on_delete=models.PROTECT, db_index=True, related_name='leads')


class Activity(CommonAttributes):
    description = models.TextField()
    lead = models.ForeignKey(
        Lead, on_delete=models.CASCADE, db_index=True, related_name='activities')
