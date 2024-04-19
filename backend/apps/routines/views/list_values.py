from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import permission_classes

from ..models import Goal, Restriction, Training, MuscleGroup
from ..constants import *
from ...main.constants import CountryChoices
from ..serializers import GoalSerializer, RestrictionSerializer, TrainingSerializer, MuscleGroupSerializer

from ...authentication.permissions import CustomerAccessPermission

@permission_classes([CustomerAccessPermission])
class ListValuesViewSet(viewsets.ModelViewSet):

    def list(self, request):
        return Response({
            "goals": GoalSerializer(Goal.objects.all(), many=True).data,
            "restrictions": RestrictionSerializer(Restriction.objects.all(), many=True).data,
            "trainings": TrainingSerializer(Training.objects.all(), many=True).data,
            "levels": LevelChoices.choices,
            "muscle_groups": MuscleGroupSerializer(MuscleGroup.objects.all(), many=True).data,
            "yes_no": YesNoChoices.choices,
            "countries": CountryChoices.choices
        })