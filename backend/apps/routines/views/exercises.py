from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.decorators import permission_classes
from rest_framework import viewsets
from rest_framework.decorators import action

from ..serializers import *
from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return super().get_queryset()