from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404

from rest_framework import viewsets, permissions
from .serializers import *


# Create your views here.
def index(request):
    return HttpResponse("<h2>index page</h2>")


def hello(request, username):
    return HttpResponse("<h2>demo %s</h2>" % username)


def routines(request, id):
    routine = get_list_or_404(
        Routine, id=id
    )  # esto es para encontrar un ID especifico, sino return nada, devuelve un 404
    routines = list(Routine.objects.values())  # trae un listado completo
    return JsonResponse(routines, safe=False)


# ViewSets define the view behavior.
class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    # serializer = BookSerializer(queryset, many=True)
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ExerciseSerializer


# ViewSets define the view behavior.
class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RoutineSerializer


class RoutineBlockViewSet(viewsets.ModelViewSet):
    queryset = RoutineDaysBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RoutineDaysBlocksSerializer


class BlocksViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = BlockSerializer


class RestrictionsViewSet(viewsets.ModelViewSet):
    queryset = Restriction.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RestrictionSerializer


class ExerciseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExerciseType.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = ExerciseTypeSerializer


class MuscleGroupViewSet(viewsets.ModelViewSet):
    queryset = MuscleGroup.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = MuscleGroupSerializer


class RoutineTypesViewSet(viewsets.ModelViewSet):
    queryset = RoutineType.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RoutineTypeSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = LevelSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = StatusSerializer


class RoutineDaysBlocksViewSet(viewsets.ModelViewSet):
    queryset = RoutineDaysBlocks.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = RoutineDaysBlocksSerializer
