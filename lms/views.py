from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from base.authenticator import authenticateUser, authenticatedUser
from lms.permissions import IsAuthenticatedEmployee


from .models import Employee, Lead
from .serializers import EmployeeCreateSerializer, EmployeeSerializer, EmployeeUpdateSerializer, LeadCreateSerializer, LeadSerializer

# Create your views here.


class DefaultPagination(PageNumberPagination):
    page_size = 100


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_active=True)
    http_method_names = ['post']
    pagination_class = DefaultPagination

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializer
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return EmployeeUpdateSerializer
        return super().get_serializer_class()


# TODO: https://www.django-rest-framework.org/api-guide/filtering/ -- find out search filter and add filter classes


class LeadViewSet(ModelViewSet):
    serializer_class = LeadSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticatedEmployee]

    pagination_class = DefaultPagination
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name', 'employee__first_name', 'email']
    # filter_classes

    def get_permissions(self):
        if self.request.method == 'POST':
            return []
        return super().get_permissions()

    def get_serializer_class(self):
        if (self.request.method == 'POST'):
            return LeadCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(employee=user).filter(is_active=True)


class GenerateToken(APIView):
    def post(self, request):
        response = authenticateUser(Employee, request)
        return response


# DONE: add token expiry validation
# DONE: create a function out of it
# DONE: create setting variable for setting

class EmployeeAPIView(APIView):
    def get(self, request):
        return authenticatedUser(Employee, EmployeeSerializer, request)


# TODO: employee viewset
class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(is_active=True)


{
    "email": "b@a.com",
    "password": "admin#123"
}

#  decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
#         print(decoded_jwt)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZW1haWwiOiJiQGEuY29tIiwidG9rZW5fZXhwaXJ5IjoiMjAyNC0wNi0wNSAxMzowNToyMS4xNDY0MDUifQ.Ov1Q5ENjJiLV88m04pkIKkYsMYgSFlY7wh-E7yFtDJc
