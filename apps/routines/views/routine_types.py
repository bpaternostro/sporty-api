from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, permissions
from ..serializers import *

class RoutineTypesViewSet(viewsets.ModelViewSet):
    queryset = RoutineType.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RoutineTypeSerializer