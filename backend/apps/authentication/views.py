import os
import jwt, datetime

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer, LoginSerializer
from .models import CustomUser, TokenWhiteList
from ..customers.models import Customer

from ..authentication.permissions import CustomerAccessPermission
from ..main.constants import TokenStatusChoices


@permission_classes([AllowAny])
class RegisterView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@permission_classes([AllowAny])
class LoginView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def create(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        django_user = authenticate(request, username=email, password=password)
        if django_user is not None:
            login(request, django_user)
        else:
            raise AuthenticationFailed('User not found!')

        payload = {
            'user_id': user.id,
            'customer_id': Customer.objects.get(customer=user).id,
            'name': user.first_name,
            'role': user.is_staff,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=int(os.getenv("EXPIRES_TOKEN_TIME"))),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        white_list_token = TokenWhiteList.objects.create(token=token)
        white_list_token.save()

        response = Response()

        #response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'Csrftoken':""
        }
        return response


@permission_classes([CustomerAccessPermission])
class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        token = request.headers.get('Authorization')
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = CustomUser.objects.filter(id=payload['user_id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


@permission_classes([CustomerAccessPermission])
class LogoutView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def create(self, request):
        response = Response()
        
        token = TokenWhiteList.objects.get(token=request.headers.get('Authorization'))
        token.status = TokenStatusChoices.EXPIRED
        token.save()
        
        logout(request)

        response.data = {
            'message': 'success'
        }
        return response