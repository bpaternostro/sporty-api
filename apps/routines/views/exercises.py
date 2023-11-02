from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404

from rest_framework import viewsets, permissions
from rest_framework.decorators import action

from ..serializers import *

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    # serializer = BookSerializer(queryset, many=True)
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return super().get_queryset()