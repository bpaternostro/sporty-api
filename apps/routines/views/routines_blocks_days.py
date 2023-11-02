from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from django.views import generic

from rest_framework import viewsets, permissions
from ..serializers import *

# ViewSets define the view behavior.
class RoutineDaysBlocksViewSet(viewsets.ModelViewSet, generic.View):
    queryset = RoutineDaysBlocks.objects.all()
    template_name = 'home/name.html'
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RoutineDaysBlocksSerializer