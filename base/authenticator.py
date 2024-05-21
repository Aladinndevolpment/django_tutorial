from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from django.contrib.auth.hashers import check_password
from jwt import encode
from django.conf import settings


def authenticateUser(model, request):
    email = request.data.get('email')
    password = request.data.get('password')
    if email is None or password is None:
        return Response({"error": "Email and password is required"}, status=status.HTTP_400_BAD_REQUEST)
    employee = model.objects.filter(email=email).first()
    if employee is None:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    if check_password(password, employee.password) == False:
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)

    expiry = datetime.now() + timedelta(days=settings.TOKEN_EXPIRY_IN_DAYS)

    payload = {
        "id": employee.id,
        "email": employee.email,
        "token_expiry": str(expiry)
    }

    encoded_jwt = encode(
        payload, "secret", algorithm="HS256")

    return encoded_jwt
