from datetime import datetime, timedelta
from django.db.models import Avg, Count
from rest_framework import serializers

from ..customers.models import Customer

from .models import (
    Exercise,
    Routine,
    RoutineDaysBlocks,
    Block,
    Restriction,
    MuscleGroup,
    RoutineDaysBlocks,
    RoutineCustomers,
    BlockExerciseDetail,
    RoutineTargetMetaData,
    RoutineCustomerIndicator,
    Goal,
    Training,
    Day
)

class ListValuesSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    label = serializers.SerializerMethodField()
    
    def get_value(self, obj):
        return obj.id

    def get_label(self, obj):
        return obj.name


class TrainingSerializer(ListValuesSerializer):
    class Meta:
        model = Training
        fields = ["value", "label"]


class GoalSerializer(ListValuesSerializer):
    class Meta:
        model = Goal
        fields = ["value", "label"]


class RestrictionSerializer(ListValuesSerializer):
    class Meta:
        model = Restriction
        fields = ["value", "label"]


class MuscleGroupSerializer(ListValuesSerializer):
    class Meta:
        model = MuscleGroup
        fields = ["value", "label"]


class BlockSerializer(serializers.ModelSerializer):
    exercises = serializers.SerializerMethodField()
    class Meta:
        model = Block
        fields = ["id", "name", "description", "creator", "status", "exercises", "type"]

    def get_exercises(self, obj):
        block_exercise = BlockExerciseDetail.objects.filter(block=obj.id)
        return BlockExerciseDetailSerializer(block_exercise, many=True).data


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
        depth = 1


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'


class RoutineCustomerIndicatorCalculationSerializer(serializers.ModelSerializer):
    
    last_training=serializers.SerializerMethodField()
    training_completed_in_last_30_days=serializers.SerializerMethodField()
    ratio_hiking=serializers.SerializerMethodField()
    completed_training=serializers.SerializerMethodField()
    ratio_welfare=serializers.SerializerMethodField()
    ratio_effort=serializers.SerializerMethodField()
    ratio_enjoyment=serializers.SerializerMethodField()


    class Meta:
        model = RoutineCustomerIndicator
        fields = ['last_training', 'training_completed_in_last_30_days', 'ratio_hiking', 'completed_training', 'ratio_welfare', 'ratio_effort', 'ratio_enjoyment']

    def get_last_training(self, obj):
        last_training = obj.all().filter(was_completed=1).order_by("-started_on")
        if len(last_training):
            return last_training[0].started_on.date().strftime('%d-%m-%Y')
        return None
    
    def get_training_completed_in_last_30_days(self, obj):
        today = datetime.now().date()
        thirty_day_before = today - timedelta(days=30)
        return obj.all().filter(started_on__gte=thirty_day_before).aggregate(Count("id"))["id__count"]
    
    def get_ratio_hiking(self, obj):
        last_training = obj.all().filter(was_completed=1).order_by("-started_on")
        if len(last_training):
            delta = datetime.now().date() - last_training[0].started_on.date()
            return delta.days
        return None
    
    def get_ratio_effort(self, obj):
        if len(obj.all()):
            return round(obj.all().aggregate(Avg('effort_scale'))["effort_scale__avg"],2)
        return 0
    
    def get_ratio_enjoyment(self, obj):
        if len(obj.all()):
            return round(obj.all().aggregate(Avg('enjoyment_scale'))["enjoyment_scale__avg"],2)
        return 0
    
    def get_completed_training(self, obj):
        return obj.all().filter(was_completed=1).aggregate(Count("id"))["id__count"]
    
    def get_ratio_welfare(self, obj):
        if len(obj.all()):
            return round(obj.all().aggregate(Avg('welfare_scale'))["welfare_scale__avg"],2)
        return 0

class RoutineTargetMetaDataSerializer(serializers.ModelSerializer):
    customer_with_equipement = serializers.SerializerMethodField()
    customer_train_at_home = serializers.SerializerMethodField()
    customer_with_lack_space = serializers.SerializerMethodField()
    customer_with_lack_time = serializers.SerializerMethodField()

    class Meta:
        model = RoutineTargetMetaData
        fields = ["min_age", "max_age", "goals", "level", "customer_with_equipement", "customer_train_at_home", "customer_with_lack_space", "customer_with_lack_time"]
        depth = 1
    
    def get_customer_with_equipement(self, obj):
        return obj.get_customer_with_equipement_display()
    
    def get_customer_train_at_home(self, obj):
        return obj.get_customer_train_at_home_display()
    
    def get_customer_with_lack_space(self, obj):
        return obj.get_customer_with_lack_space_display()

    def get_customer_with_lack_time(self, obj):
        return obj.get_customer_with_lack_time_display()


class RoutineDaysBlocksSerializer(serializers.ModelSerializer):
    blocks = serializers.SerializerMethodField()
    class Meta:
        model = RoutineDaysBlocks
        fields = ["day", "blocks"]
        depth = 1

    def get_blocks(self, obj):
        blocks = obj.blocks
        return BlockSerializer(blocks, many=True).data


class RoutineSerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()
    days = serializers.SerializerMethodField()
    status_routine = serializers.SerializerMethodField()
    start_date = serializers.SerializerMethodField()
    due_date = serializers.SerializerMethodField()
    observation = serializers.SerializerMethodField()
    
    class Meta:
        model = Routine
        fields = ["id", "info", "days", "status_routine", "start_date", "due_date", "observation"]
        depth = 1
        
    def get_info(self, obj):
        return RoutineSerializerDetail(obj).data
    
    def get_days(self, obj):
        routine_day_blocks = RoutineDaysBlocks.objects.filter(routine=obj.id).order_by("day")
        return RoutineDaysBlocksSerializer(routine_day_blocks, many=True).data
    
    def get_status_routine(self, obj):
        customer_routine = RoutineCustomers.objects.filter(routine=obj).order_by("start_date")
        return customer_routine[0].status
    
    def get_start_date(self, obj):
        customer_routine = RoutineCustomers.objects.filter(routine=obj).order_by("start_date")
        return customer_routine[0].start_date.strftime('%d-%m-%Y')
    
    def get_due_date(self, obj):
        customer_routine = RoutineCustomers.objects.filter(routine=obj).order_by("start_date")
        return customer_routine[0].due_date.strftime('%d-%m-%Y')

    def get_observation(self, obj):
        customer_routine = RoutineCustomers.objects.filter(routine=obj).order_by("start_date")
        return customer_routine[0].observation
    

class RoutineSerializerDetail(serializers.ModelSerializer):
    routine_metadata = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    routine_type = serializers.SerializerMethodField()
    system = serializers.SerializerMethodField()
    cadence = serializers.SerializerMethodField()
    pre_exhaustion = serializers.SerializerMethodField()
    activation = serializers.SerializerMethodField()
    training_method = serializers.SerializerMethodField()
    days_of_week = serializers.SerializerMethodField()

    class Meta:
        model = Routine
        fields = "__all__"
        depth = 1
    
    def get_routine_metadata(self, obj):
        routine_goals = RoutineTargetMetaData.objects.filter(routine=obj.id)
        return RoutineTargetMetaDataSerializer(routine_goals, many=True).data

    def get_status(self, obj):
        return obj.get_status_display()

    def get_routine_type(self, obj):
        return obj.get_routine_type_display()
    
    def get_system(self, obj):
        return obj.get_system_display()

    def get_cadence(self, obj):
        return obj.get_cadence_display()
    
    def get_pre_exhaustion(self, obj):
        return obj.get_pre_exhaustion_display()
    
    def get_activation(self, obj):
        return obj.get_activation_display()

    def get_training_method(self, obj):
        return obj.get_training_method_display()
    
    def get_days_of_week(self, obj):
        return DaySerializer(obj.days_of_week.order_by('id'), many=True).data
    

class BlockExerciseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockExerciseDetail
        fields = ["exercise", "serie", "reps", "weight", "pause", "observation"]
        depth = 1
