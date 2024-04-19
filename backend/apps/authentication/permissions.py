import jwt

from rest_framework import permissions

from django.conf import settings

from .models import TokenWhiteList

from ..main.constants import TokenStatusChoices

class CustomerAccessPermission(permissions.BasePermission):
    message = 'JWT Auth Required.'

    def has_permission(self, request, view):
        token = request.headers.get('Authorization')
        try:
            token_from_white_list = TokenWhiteList.objects.get(token=token)
            if not token or token_from_white_list.status == TokenStatusChoices.EXPIRED.value:
                return False
        except Exception as e:
            return False

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return False
        
        return True