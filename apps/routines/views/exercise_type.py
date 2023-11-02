from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404

from rest_framework import viewsets, permissions
from ..serializers import *

class ExerciseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExerciseType.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ExerciseTypeSerializer