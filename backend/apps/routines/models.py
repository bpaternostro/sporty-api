from django.db import models
from django.conf import settings

from ..main.models import FitboxBaseModel, FitboxBaseRelationsModel, FitboxBaseWithIimageModel
from .constants import *
from ..customers.constants import *

class RoutineCustomers(FitboxBaseRelationsModel):
    customer = models.ForeignKey("customers.Customer", on_delete=models.DO_NOTHING)
    routine = models.ForeignKey('Routine', on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.IN_PROGRESS)
    observation = models.TextField()
    start_date = models.DateField(blank=True)
    due_date = models.DateField(blank=True)

    class Meta:
        verbose_name = "Routine customers"
        verbose_name_plural = "Routine customers"


class RoutineCustomerIndicator(FitboxBaseRelationsModel):
    customer = models.ForeignKey("customers.Customer", on_delete=models.DO_NOTHING)
    routine = models.ForeignKey('Routine', on_delete=models.DO_NOTHING)
    started_on = models.DateTimeField()
    finished_on = models.DateTimeField(auto_now_add=True)
    welfare_scale = models.IntegerField(default=1)
    effort_scale = models.IntegerField(default=1)
    enjoyment_scale = models.IntegerField(default=1)
    was_completed = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.YES)
    
    class Meta:
        verbose_name = "Routine customers indicators"
        verbose_name_plural = "Routine customers indicators"


class MuscleGroup(FitboxBaseWithIimageModel):
    muscle_group_type = models.IntegerField(choices=MuscleGroupTypeChoices.choices, default=MuscleGroupTypeChoices.CORE)


class Restriction(FitboxBaseWithIimageModel):
    pass


class Day(FitboxBaseWithIimageModel):
    pass


class Goal(FitboxBaseWithIimageModel):
    pass


class Level(FitboxBaseWithIimageModel):
    pass


class Training(FitboxBaseWithIimageModel):
    pass

class Exercise(FitboxBaseWithIimageModel):
    description = models.TextField()
    type = models.IntegerField(choices=ExerciseTypeChoices.choices, default=ExerciseTypeChoices.MOVILITY)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.IN_PROGRESS)
    video_link = models.URLField(blank=True)
    creator = models.ForeignKey("authentication.CustomUser", on_delete=models.DO_NOTHING)
    muscle_group = models.ManyToManyField(MuscleGroup, blank=True)
    level = models.ForeignKey(Level, on_delete=models.DO_NOTHING)


class Block(FitboxBaseModel):
    status = models.IntegerField(choices = StatusChoices.choices, default=StatusChoices.IN_PROGRESS)
    creator = models.ForeignKey("authentication.CustomUser", on_delete=models.DO_NOTHING)
    exercises = models.ManyToManyField(Exercise, through='BlockExerciseDetail', blank=True)
    type = models.IntegerField(choices = BlockTypeChoices.choices)
    description = models.TextField()


class BlockExerciseDetail(FitboxBaseRelationsModel):
    block = models.ForeignKey(Block, on_delete=models.DO_NOTHING, default=1)
    exercise = models.ForeignKey(Exercise, on_delete=models.DO_NOTHING)
    serie = models.IntegerField(blank=True, null=True)
    reps = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    weight = models.CharField(max_length=10, blank=True, null=True)
    pause = models.CharField(max_length=10, blank=True, null=True)
    observation = models.TextField(blank=True, null=True)


class Routine(FitboxBaseModel):
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.IN_PROGRESS)
    description = models.TextField()
    routine_type = models.IntegerField(choices=RoutineTypeChoices.choices, default=RoutineTypeChoices.MONTHLY)
    restrictions = models.ManyToManyField(Restriction, blank=True)
    creator = models.ForeignKey("authentication.CustomUser", on_delete=models.DO_NOTHING)
    system = models.IntegerField(choices=SystemChoices.choices, default=SystemChoices.DRH)
    cadence = models.IntegerField(choices=CadenceChoices.choices, default=CadenceChoices.CLASSIC)
    cardio = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    pre_exhaustion = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    activation = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    rest_between_exercises = models.CharField(max_length=50)
    days_of_week = models.ManyToManyField(Day, through="RoutineDaysBlocks", blank=True)
    training_method = models.IntegerField(choices=TrainingMethodChoices.choices, default=TrainingMethodChoices.STRENGTH)


class RoutineTargetMetaData(FitboxBaseRelationsModel):
    routine = models.OneToOneField(Routine, on_delete=models.CASCADE)
    min_age = models.IntegerField(blank=True, null=True)
    max_age = models.IntegerField(blank=True, null=True)
    goals = models.ManyToManyField(Goal, blank=True)
    level = models.ManyToManyField(Level, blank=True)
    customer_with_equipement = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    customer_train_at_home = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    customer_with_lack_space = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    customer_with_lack_time = models.IntegerField(choices=YesNoChoices.choices, default=YesNoChoices.NO)
    

class RoutineDaysBlocks(FitboxBaseRelationsModel):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    blocks = models.ManyToManyField(Block, blank=True)
