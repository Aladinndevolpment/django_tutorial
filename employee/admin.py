# TODO: Remove repetition. (created_at, updated_at, is_active)
from typing import Any
from django.contrib import admin


from import_export.admin import ImportExportModelAdmin
from .models import Department, Designation, Employee, \
    AddressInformation

from django.contrib.auth.hashers import make_password
# Register your models here.


class CommonAdminAttributes(ImportExportModelAdmin):
    list_display = ['created_at', 'update_at', 'is_active']


@admin.register(Department)
class DepartmentAdmin(CommonAdminAttributes):
    list_display = ['id', 'name', 'code', 'description'] + \
        CommonAdminAttributes.list_display
    search_fields = ['name']
    list_filter = ['created_at']
    list_editable = ['is_active']


@admin.register(Designation)
class DesignationAdmin(CommonAdminAttributes):
    list_display = ['id', 'department', 'description'] + \
        CommonAdminAttributes.list_display
    autocomplete_fields = ['department']


class AddressInline(admin.StackedInline):
    model = AddressInformation
    extra = 0


# TODO: Add autocomplete for designation
# TODO: Add documents inline.
@admin.register(Employee)
class EmployeeAdmin(CommonAdminAttributes):
    list_display = ['first_name', 'last_name', 'email', 'get_designation_description',
                    'contact'] + CommonAdminAttributes.list_display
    inlines = [AddressInline]

    def get_designation_description(self, obj):
        return obj.designation.description

    def save_model(self, request, obj: Any, form, change):
        if not change and not obj.pk:
            obj.password = make_password(obj.password)
        elif change and obj.password != obj.__class__.objects.get(pk=obj.pk).password:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)
