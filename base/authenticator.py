from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from django.contrib.auth.hashers import check_password
from jwt import encode, decode
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

    return Response({"token": encoded_jwt, "message": "Authentication successful."}, status=status.HTTP_200_OK)


def authenticatedUser(model, serializer, request):
    if 'Authorization' not in request.headers:
        return Response({"error": "Authorization header is required."},
                        status=status.HTTP_403_FORBIDDEN)
    authorization: str = request.headers['Authorization']

    if 'Bearer' not in authorization:
        return Response({"error": "Token is malformed."},
                        status=status.HTTP_400_BAD_REQUEST)

    authorization = authorization.split(' ')[1].strip()

    user = decode(authorization, 'secret', algorithms=["HS256"])
    current_time = datetime.now()
    token_exp = datetime.strptime(user['token_expiry'], "%Y-%m-%d %H:%M:%S.%f")

    if token_exp < current_time:
        return Response({"error": "Token is expired."},
                        status=status.HTTP_403_FORBIDDEN)

    eid = user['id']
    employee = model.objects.filter(id=eid).first()

    return Response({"employee": serializer(employee).data, "message": "Authentication successful."}, status=status.HTTP_200_OK)
