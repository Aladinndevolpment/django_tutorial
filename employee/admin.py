# TODO: Remove repetition. (created_at, updated_at, is_active)
from django.contrib import admin
from .models import Department, Designation
# Register your models here.


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code',
                    'description', 'created_at', 'update_at', 'is_active']
    search_fields = ['name']
    list_filter = ['created_at']
    list_editable = ['is_active']


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ['id', 'department', 'description',
                    'created_at', 'update_at', 'is_active']
