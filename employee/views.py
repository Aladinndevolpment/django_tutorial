from rest_framework.viewsets import ModelViewSet

from employee.serializer import EmployeeSerializer, AllEmployeeSerializer
from .models import Employee

# Create your views here.


# TODO: Encrypt password.
class EmployeeProfileViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post']


class AllEmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.filter(is_active=True)
    serializer_class = AllEmployeeSerializer
