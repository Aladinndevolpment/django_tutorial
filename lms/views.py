from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Employee, Lead
from .serializers import EmployeeCreateSerializer, EmployeeSerializer, EmployeeUpdateSerializer, LeadSerializer

# Create your views here.


class DefaultPagination(PageNumberPagination):
    page_size = 100


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_active=True)
    http_method_names = ['get', 'put', 'post']
    pagination_class = DefaultPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return EmployeeUpdateSerializer
        return super().get_serializer_class()


class LeadViewSet(ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.filter(is_active=True)
    http_method_names = ['get', 'post']
