from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404
from .models import Exercise, Routine, RoutineDaysBlocks, Block
from rest_framework import serializers, viewsets, permissions


# Serializers define the API representation.
class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
        depth = 1


class RoutineDaysBlocksSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)

    class Meta:
        model = RoutineDaysBlocks
        fields = "__all__"


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"
        depth = 1


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
