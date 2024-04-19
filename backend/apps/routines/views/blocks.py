from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.decorators import permission_classes
from rest_framework import viewsets, permissions

from ..serializers import *
from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class BlocksViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
