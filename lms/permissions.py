from rest_framework.permissions import BasePermission

from base.authenticator import authenticatedUser
from .models import Employee
from .serializers import EmployeeSerializer


# TODO: Set response from authenticatedUser
class IsAuthenticatedEmployee(BasePermission):
    def has_permission(self, request, view):
        response = authenticatedUser(Employee, EmployeeSerializer, request)
        if response.status_code == 400 or response.status_code == 403:
            return False

        request.user = response.data['employee']['id']
        request.user_data = response.data['employee']
        return response.data
