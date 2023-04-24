from rest_framework import serializers
from .models import (
    Exercise,
    Routine,
    RoutineDaysBlocks,
    Block,
    Status,
    Restriction,
    RoutineType,
    ExerciseType,
    MuscleGroup,
    RoutineDaysBlocks,
    Level,
)


# Serializers define the API representation.
class RestrictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restriction
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = "__all__"


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = "__all__"


class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = "__all__"


class RoutineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineType
        fields = "__all__"


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
        depth = 1


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
