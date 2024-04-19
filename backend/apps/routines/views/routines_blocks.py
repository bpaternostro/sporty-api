from rest_framework.decorators import permission_classes
from rest_framework import viewsets

from ..serializers import *
from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class RoutineBlockViewSet(viewsets.ModelViewSet):
    queryset = RoutineDaysBlocks.objects.all()
    serializer_class = RoutineDaysBlocksSerializer
