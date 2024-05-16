from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Employee, Lead


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['is_active', 'password']

    def create(self, validated_data):
        hash = make_password(validated_data['password'])
        validated_data['password'] = hash
        return super().create(validated_data)


class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['is_active']

# TODO: Add employee to POST.


class LeadSerializer(serializers.ModelSerializer):
    employee = serializers.SerializerMethodField('get_employee_name')

    def get_employee_name(self, lead):
        return {"first_name": lead.employee.first_name, "id": lead.employee.id}

    class Meta:
        model = Lead
        exclude = ['is_active']


class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['is_active', 'email', 'password']
