from django.contrib import admin

from lms.models import Employee, Lead

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name']


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['id']
