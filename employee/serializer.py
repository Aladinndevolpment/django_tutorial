# TODO: create serializers for designation and department.

from rest_framework import serializers
from .models import Employee, AddressInformation


# TODO: define needed fields only.
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressInformation
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name='get_full_name')
    addresses = AddressSerializer(many=True)
    # address = serializers.SerializerMethodField(method_name='get_address')

    # def get_address(self, employee):
    #     return employee.addresses[0]

    def get_full_name(self, employee):
        return employee.first_name + " " + employee.last_name

    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'addresses',
                  'designation']
