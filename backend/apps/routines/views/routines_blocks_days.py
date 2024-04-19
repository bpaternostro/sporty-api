from django.views import generic
from rest_framework.decorators import permission_classes
from rest_framework import viewsets

from ..serializers import *
from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class RoutineDaysBlocksViewSet(viewsets.ModelViewSet, generic.View):
    queryset = RoutineDaysBlocks.objects.all()
    template_name = 'home/name.html'
    serializer_class = RoutineDaysBlocksSerializer