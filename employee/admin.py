# TODO: Remove repetition. (created_at, updated_at, is_active)
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Department, Designation, Employee
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


# TODO: Add autocomplete for designation
@admin.register(Employee)
class EmployeeAdmin(CommonAdminAttributes):
    list_display = ['first_name', 'last_name', 'email', 'get_designation_description',
                    'contact'] + CommonAdminAttributes.list_display

    def get_designation_description(self, obj):
        return obj.designation.description
