from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from jwt import decode
from rest_framework.pagination import PageNumberPagination

from base.authenticator import authenticateUser


from .models import Employee, Lead
from .serializers import EmployeeCreateSerializer, EmployeeSerializer, EmployeeUpdateSerializer, LeadSerializer

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


class LeadViewSet(ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.filter(is_active=True)
    http_method_names = ['get', 'post']


class GenerateToken(APIView):
    def post(self, request):
        jwt = authenticateUser(Employee, request)
        return Response({"token": jwt, "message": "Authentication successful."}, status=status.HTTP_200_OK)


# TODO: add token expiry validation
# TODO: create a function out of it
# TODO: create setting variable for setting

class EmployeeAPIView(APIView):
    def get(self, request):
        if 'Authorization' not in request.headers:
            return Response({"error": "Authorization header is required."},
                            status=status.HTTP_403_FORBIDDEN)
        authorization: str = request.headers['Authorization']

        if 'Bearer' not in authorization:
            return Response({"error": "Token is malformed."},
                            status=status.HTTP_400_BAD_REQUEST)

        authorization = authorization.split(' ')[1].strip()

        user = decode(authorization, 'secret', algorithms=["HS256"])
        eid = user['id']
        employee = Employee.objects.filter(id=eid).first()

        return Response({"employee": employee.first_name, "message": "Authentication successful."}, status=status.HTTP_200_OK)


{
    "email": "b@a.com",
    "password": "admin#123"
}

#  decoded_jwt = jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
#         print(decoded_jwt)
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NSwiZW1haWwiOiJiQGEuY29tIiwidG9rZW5fZXhwaXJ5IjoiMjAyNC0wNi0wNSAxMzowNToyMS4xNDY0MDUifQ.Ov1Q5ENjJiLV88m04pkIKkYsMYgSFlY7wh-E7yFtDJc
