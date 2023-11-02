from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404

from rest_framework import viewsets, permissions
from ..serializers import *

class RoutineBlockViewSet(viewsets.ModelViewSet):
    queryset = RoutineDaysBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RoutineDaysBlocksSerializer
