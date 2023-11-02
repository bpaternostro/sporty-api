from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, permissions
from ..serializers import *

class StatusViewSet(viewsets.ModelViewSet):
    queryset = RoutineStatus.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = StatusSerializer