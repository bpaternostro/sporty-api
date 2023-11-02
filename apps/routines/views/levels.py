from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, permissions
from ..serializers import *

class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = LevelSerializer